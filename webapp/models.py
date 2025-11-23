from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    given_name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(30))
    profile_description = db.Column(db.Text)
    password = db.Column(db.String(255), nullable=False)

class Caregiver(db.Model):
    __tablename__ = "caregiver"
    caregiver_user_id = db.Column(db.Integer, db.ForeignKey("user.user_id", ondelete="CASCADE"), primary_key=True)
    photo = db.Column(db.Text)
    gender = db.Column(db.String(20), nullable=False)
    caregiving_type = db.Column(db.String(30), nullable=False)
    hourly_rate = db.Column(db.Numeric(6, 2), nullable=False)

class Member(db.Model):
    __tablename__ = "member"
    member_user_id = db.Column(db.Integer, db.ForeignKey("user.user_id", ondelete="CASCADE"), primary_key=True)
    house_rules = db.Column(db.Text)
    dependent_description = db.Column(db.Text)

class Address(db.Model):
    __tablename__ = "address"
    member_user_id = db.Column(db.Integer, db.ForeignKey("member.member_user_id", ondelete="CASCADE"), primary_key=True)
    house_number = db.Column(db.String(20))
    street = db.Column(db.String(100), nullable=False)
    town = db.Column(db.String(100))

class Job(db.Model):
    __tablename__ = "job"
    job_id = db.Column(db.Integer, primary_key=True)
    member_user_id = db.Column(db.Integer, db.ForeignKey("member.member_user_id", ondelete="CASCADE"), nullable=False)
    required_caregiving_type = db.Column(db.String(30), nullable=False)
    other_requirements = db.Column(db.Text)
    date_posted = db.Column(db.Date)

class JobApplication(db.Model):
    __tablename__ = "job_application"
    caregiver_user_id = db.Column(db.Integer, db.ForeignKey("caregiver.caregiver_user_id", ondelete="CASCADE"), primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey("job.job_id", ondelete="CASCADE"), primary_key=True)
    date_applied = db.Column(db.Date)

class Appointment(db.Model):
    __tablename__ = "appointment"
    appointment_id = db.Column(db.Integer, primary_key=True)
    caregiver_user_id = db.Column(db.Integer, db.ForeignKey("caregiver.caregiver_user_id", ondelete="CASCADE"), nullable=False)
    member_user_id = db.Column(db.Integer, db.ForeignKey("member.member_user_id", ondelete="CASCADE"), nullable=False)
    appointment_date = db.Column(db.Date, nullable=False)
    appointment_time = db.Column(db.Time, nullable=False)
    work_hours = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)
