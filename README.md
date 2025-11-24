Team members:

Daniyar Kshibekov,
Askar Matayev

# CSCI 341 Assignment 3 — Caregivers Platform

## 1) Create DB and tables
1. Create database `care_platform_db` in PostgreSQL.
2. Run:
   - sql/01_create_tables.sql
   - sql/02_insert_data.sql

## 2) Run Part 2 script
Edit credentials in python/main.py, then:
```bash
cd python
python main.py

# Care Platform Database Project
CSCI 341 - Database Management Systems - Assignment 3

## Project Overview
An online caregiver platform connecting families with caregivers (babysitters, elderly care, playmates).

## Setup Instructions

### 1. Database Setup
```bash
# Install PostgreSQL if not already installed
# Create database
createdb -U postgres care_platform_db

# Or using psql:
psql -U postgres
CREATE DATABASE care_platform_db;
\q
```

### 2. Python Environment
```bash
# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Database Password
Update the password in:
- `python/main.py` (line 6)
- `webapp/app.py` (line 9)

Replace `YOUR_PASSWORD` with your PostgreSQL password.

### 4. Run Part 1 & 2 (Database + Queries)
```bash
cd python
python main.py
```

This will:
- Create all tables
- Insert sample data (10+ rows per table)
- Run all queries (UPDATE, DELETE, SELECT, etc.)

### 5. Run Part 3 (Web Application)
```bash
cd webapp
python app.py
```

Visit: http://localhost:5000

## Project Structure
```
DATABASE-ASSIGNMENT/
├── python/
│   └── main.py              # Part 2: SQLAlchemy queries
├── sql/
│   ├── 01_create_tables.sql # Part 1: Table creation
│   └── 02_insert_data.sql   # Part 1: Sample data
├── webapp/
│   ├── app.py              # Part 3: Flask application
│   ├── models.py           # SQLAlchemy models
│   └── templates/          # HTML templates
├── report/
│   └── executive_summary.md
└── requirements.txt
```

## Features Implemented
✅ Part 1: Database schema with 7 tables, 10+ rows each
✅ Part 2: All required queries (UPDATE, DELETE, SELECT, VIEW)
✅ Part 3: Full CRUD web application

## Team Members
[Add your names here]