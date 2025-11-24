 Daniyar Kshibekov
 Askar Matayev


1. Database Design (Part 1)
We created all required tables exactly according to the schema: USER, CAREGIVER, MEMBER, ADDRESS, JOB, JOB_APPLICATION, and APPOINTMENT.
All primary and foreign keys were added, together with reasonable constraints (e.g., checking valid caregiving types, enforcing cascading deletes, and limiting invalid values).
We inserted at least 10 records into every table so that all required queries from Part 2 return meaningful results.

2. SQL Queries Through Python (Part 2)
Using Python and SQLAlchemy, we executed all types of operations:

Creating tables

Inserting sample data

Update queries (changing phone numbers, adjusting hourly rates)

Delete queries (e.g., removing jobs by a specific member)

Four simple queries and four complex queries involving multiple joins and aggregations

A query with a derived attribute (calculating total appointment cost)

A VIEW that lists job applications with applicant details

All queries were run successfully, and the results were non-empty as required.

3. Web Application (Part 3)
We built a basic Flask application that provides Create, Read, Update, and Delete operations for all seven tables. The interface is simple, but functionality works as intended.
We handled special cases like the composite primary key in the JOB_APPLICATION table, and the site connects correctly to the hosted database.
The app was deployed on a public hosting service (Render), and the link is included in the submission.