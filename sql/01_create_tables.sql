-- Part 1: Create tables according to the given schema
-- DBMS: PostgreSQL
-- If you already created tables, running again is safe because of IF NOT EXISTS.

CREATE TABLE IF NOT EXISTS "user" (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    given_name VARCHAR(100) NOT NULL,
    surname VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    phone_number VARCHAR(30),
    profile_description TEXT,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS caregiver (
    caregiver_user_id INT PRIMARY KEY,
    photo TEXT,
    gender VARCHAR(20) NOT NULL CHECK (gender IN ('Male', 'Female', 'Other')),
    caregiving_type VARCHAR(30) NOT NULL CHECK (caregiving_type IN ('Babysitter', 'Elderly Care', 'Playmate')),
    hourly_rate NUMERIC(6,2) NOT NULL CHECK (hourly_rate > 0),
    CONSTRAINT fk_caregiver_user
        FOREIGN KEY (caregiver_user_id)
        REFERENCES "user"(user_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS member (
    member_user_id INT PRIMARY KEY,
    house_rules TEXT,
    dependent_description TEXT,
    CONSTRAINT fk_member_user
        FOREIGN KEY (member_user_id)
        REFERENCES "user"(user_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS address (
    member_user_id INT PRIMARY KEY,
    house_number VARCHAR(20),
    street VARCHAR(100) NOT NULL,
    town VARCHAR(100),
    CONSTRAINT fk_address_member
        FOREIGN KEY (member_user_id)
        REFERENCES member(member_user_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS job (
    job_id SERIAL PRIMARY KEY,
    member_user_id INT NOT NULL,
    required_caregiving_type VARCHAR(30) NOT NULL CHECK (required_caregiving_type IN ('Babysitter', 'Elderly Care', 'Playmate')),
    other_requirements TEXT,
    date_posted DATE NOT NULL DEFAULT CURRENT_DATE,
    CONSTRAINT fk_job_member
        FOREIGN KEY (member_user_id)
        REFERENCES member(member_user_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS job_application (
    caregiver_user_id INT NOT NULL,
    job_id INT NOT NULL,
    date_applied DATE NOT NULL DEFAULT CURRENT_DATE,
    PRIMARY KEY (caregiver_user_id, job_id),
    CONSTRAINT fk_jobapp_caregiver
        FOREIGN KEY (caregiver_user_id)
        REFERENCES caregiver(caregiver_user_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_jobapp_job
        FOREIGN KEY (job_id)
        REFERENCES job(job_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS appointment (
    appointment_id SERIAL PRIMARY KEY,
    caregiver_user_id INT NOT NULL,
    member_user_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    appointment_time TIME NOT NULL,
    work_hours INT NOT NULL CHECK (work_hours > 0),
    status VARCHAR(20) NOT NULL CHECK (status IN ('Pending', 'Accepted', 'Declined')),
    CONSTRAINT fk_appt_caregiver
        FOREIGN KEY (caregiver_user_id)
        REFERENCES caregiver(caregiver_user_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_appt_member
        FOREIGN KEY (member_user_id)
        REFERENCES member(member_user_id)
        ON DELETE CASCADE
);
