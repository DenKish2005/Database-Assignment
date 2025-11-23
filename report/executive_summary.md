# Executive Summary - Assignment 3 (CSCI 341)

## What was implemented
- Part 1: Physical database in PostgreSQL with all tables created according to the given schema. Each table contains at least 10 instances.
- Part 2: Python script using SQLAlchemy that connects to the database and executes all required create/insert/update/delete/simple/complex/derived/view queries.
- Part 3: Flask web application with CRUD operations for every table.

## Design assumptions
- Enumerations were implemented using CHECK constraints:
  - caregiving_type ∈ {Babysitter, Elderly Care, Playmate}
  - gender ∈ {Male, Female, Other}
  - appointment status ∈ {Pending, Accepted, Declined}
- Cascading deletes were used to keep referential integrity.

## Notes / Limitations
- User interface was kept minimal since UI is not graded.
- Deployment steps are documented in README.

## Tech stack
PostgreSQL, Python 3, SQLAlchemy, Flask, Flask-SQLAlchemy.
