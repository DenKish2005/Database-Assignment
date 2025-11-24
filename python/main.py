from sqlalchemy import create_engine, text


DB_USER = "postgres"
DB_PASSWORD = "Gumballdarwin1385"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "care_platform_db"

ENGINE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(ENGINE_URL, echo=False)


def run(sql: str, title: str = None, fetch: bool = True):
    if title:
        print("\n" + "=" * 80)
        print(title)
        print("=" * 80)
    with engine.begin() as conn:
        result = conn.execute(text(sql))
        if fetch:
            rows = result.fetchall()
            for r in rows:
                print(r)
            return rows
        return None


def create_tables():
    print("\n[1] creating tables...")       
    create_sql = open("../sql/01_create_tables.sql", "r", encoding="utf-8").read()
    with engine.begin() as conn:
        conn.execute(text(create_sql))
    print("DONE")      


def seed_data_if_empty():
    print("\n[2] Inserting data if emmpty")
    count_users = run('SELECT COUNT(*) FROM "user";', fetch=True)[0][0]
    if count_users == 0:
        insert_sql = open("../sql/02_insert_data.sql", "r", encoding="utf-8").read()
        with engine.begin() as conn:
            conn.execute(text(insert_sql))
        print("DONE")        
    else:
        print("Already has it!!! Skipping seed.")


def part2_queries():    

    run("""
        UPDATE "user"   
        SET phone_number = '+77773414141'   
        WHERE given_name = 'Arman' AND surname = 'Armanov';
    """, title="[3.1] Update phone number of Arman Armanov", fetch=False)

    run("""
        SELECT user_id, given_name, surname, phone_number
        FROM "user"
        WHERE given_name='Arman' AND surname='Armanov';
    """, title="Check Arman phone after update")

    run(""" 
        UPDATE caregiver
        SET hourly_rate =   
            CASE
                WHEN hourly_rate < 10 THEN hourly_rate + 0.3
                ELSE hourly_rate * 1.10
            END;        
    """, title="[3.2] Add commission fee to caregiver hourly rates", fetch=False)

    run(""" 
        SELECT caregiver_user_id, caregiving_type, hourly_rate
        FROM caregiver      
        ORDER BY caregiver_user_id;                 
    """, title="Check caregiver rates after commission")


    run("""
        DELETE FROM job     
        WHERE member_user_id IN (
            SELECT u.user_id
            FROM "user" u
            WHERE u.given_name='Amina' AND u.surname='Aminova'
        );
    """, title="[4.1] Delete jobs posted by Amina Aminova", fetch=False)

    run("""
        DELETE FROM member
        WHERE member_user_id IN (
            SELECT member_user_id
            FROM address
            WHERE street='Kabanbay Batyr'
        );
    """, title="[4.2] Delete all members who live on Kabanbay Batyr street", fetch=False)

    run("""
        SELECT cu.given_name || ' ' || cu.surname AS caregiver_name,
               mu.given_name || ' ' || mu.surname AS member_name
        FROM appointment a
        JOIN caregiver c ON a.caregiver_user_id = c.caregiver_user_id
        JOIN member m ON a.member_user_id = m.member_user_id
        JOIN "user" cu ON cu.user_id = c.caregiver_user_id
        JOIN "user" mu ON mu.user_id = m.member_user_id
        WHERE a.status='Accepted';
    """, title="[5.1] Caregiver and member names for accepted appointments")

    run("""
        SELECT job_id
        FROM job
        WHERE other_requirements ILIKE '%soft-spoken%';
    """, title="[5.2] Job IDs containing 'soft-spoken'")

    run("""
        SELECT a.work_hours
        FROM appointment a
        JOIN caregiver c ON a.caregiver_user_id = c.caregiver_user_id
        WHERE c.caregiving_type='Babysitter';
    """, title="[5.3] Work hours of all babysitter positions")

    run("""
        SELECT DISTINCT mu.given_name, mu.surname
        FROM member m
        JOIN "user" mu ON mu.user_id = m.member_user_id
        JOIN job j ON j.member_user_id = m.member_user_id
        WHERE j.required_caregiving_type='Elderly Care'
          AND mu.city='Astana'
          AND m.house_rules ILIKE '%No pets.%';
    """, title="[5.4] Members looking for Elderly Care in Astana with 'No pets.'")

    run("""
        SELECT j.job_id, mu.given_name || ' ' || mu.surname AS member_name,
               COUNT(ja.caregiver_user_id) AS applicant_count
        FROM job j
        JOIN member m ON j.member_user_id = m.member_user_id
        JOIN "user" mu ON mu.user_id = m.member_user_id
        LEFT JOIN job_application ja ON ja.job_id = j.job_id
        GROUP BY j.job_id, member_name
        ORDER BY j.job_id;
    """, title="[6.1] Number of applicants per job")

    run("""
        SELECT cu.given_name || ' ' || cu.surname AS caregiver_name,
               SUM(a.work_hours) AS total_hours
        FROM appointment a
        JOIN caregiver c ON a.caregiver_user_id=c.caregiver_user_id
        JOIN "user" cu ON cu.user_id=c.caregiver_user_id
        WHERE a.status='Accepted'
        GROUP BY caregiver_name
        ORDER BY total_hours DESC;
    """, title="[6.2] Total hours by caregivers for accepted appointments")

    run("""
        SELECT cu.given_name || ' ' || cu.surname AS caregiver_name,
               AVG(c.hourly_rate) AS avg_pay
        FROM appointment a
        JOIN caregiver c ON a.caregiver_user_id=c.caregiver_user_id
        JOIN "user" cu ON cu.user_id=c.caregiver_user_id
        WHERE a.status='Accepted'
        GROUP BY caregiver_name
        ORDER BY avg_pay DESC;
    """, title="[6.3] Average pay of caregivers based on accepted appointments")

    run("""
        SELECT caregiver_name, avg_pay
        FROM (
            SELECT cu.given_name || ' ' || cu.surname AS caregiver_name,
                   AVG(c.hourly_rate) AS avg_pay
            FROM appointment a
            JOIN caregiver c ON a.caregiver_user_id=c.caregiver_user_id
            JOIN "user" cu ON cu.user_id=c.caregiver_user_id
            WHERE a.status='Accepted'
            GROUP BY caregiver_name
        ) t
        WHERE avg_pay > (
            SELECT AVG(c2.hourly_rate)
            FROM appointment a2
            JOIN caregiver c2 ON a2.caregiver_user_id = c2.caregiver_user_id
            WHERE a2.status='Accepted'
        );
    """, title="[6.4] Caregivers who earn above average (accepted appointments)")

    run("""
        SELECT a.appointment_id,
               cu.given_name || ' ' || cu.surname AS caregiver_name,
               mu.given_name || ' ' || mu.surname AS member_name,
               a.work_hours,
               c.hourly_rate,   
               (a.work_hours * c.hourly_rate) AS total_cost
        FROM appointment a  
        JOIN caregiver c ON a.caregiver_user_id=c.caregiver_user_id
        JOIN member m ON a.member_user_id=m.member_user_id
        JOIN "user" cu ON cu.user_id=c.caregiver_user_id
        JOIN "user" mu ON mu.user_id=m.member_user_id
        WHERE a.status='Accepted'   
        ORDER BY a.appointment_id;
    """, title="[7] Total cost for all accepted appointments")

    run("""     
        CREATE OR REPLACE VIEW job_applications_view AS
        SELECT j.job_id,        
               j.required_caregiving_type,
               mu.given_name || ' ' || mu.surname AS member_name,
               cu.given_name || ' ' || cu.surname AS caregiver_name,
               c.caregiving_type AS caregiver_type,
               ja.date_applied
        FROM job_application ja
        JOIN job j ON ja.job_id=j.job_id
        JOIN caregiver c ON ja.caregiver_user_id=c.caregiver_user_id
        JOIN member m ON j.member_user_id=m.member_user_id          
        JOIN "user" cu ON cu.user_id=c.caregiver_user_id
        JOIN "user" mu ON mu.user_id=m.member_user_id;
    """, title="[8] Create VIEW job_applications_view", fetch=False)

    run("""
        SELECT *        
        FROM job_applications_view
        ORDER BY job_id, caregiver_name;
    """, title="Select from VIEW job_applications_view")


def main():
    create_tables() 
    seed_data_if_empty()
    part2_queries() 


if __name__ == "__main__":
    main()  
