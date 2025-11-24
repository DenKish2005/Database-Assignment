INSERT INTO "user"(email, given_name, surname, city, phone_number, profile_description, password) VALUES
('arman1@mail.com','Arman','Armanov','Almaty','+77001110001','Experienced babysitter','pass1'),
('aigerim2@mail.com','Aigerim','Nurzhanova','Astana','+77001110002','Elderly caregiver','pass2'),
('timur3@mail.com','Timur','Sadykov','Almaty','+77001110003','Playmate for children','pass3'),
('dina4@mail.com','Dina','Kassymova','Shymkent','+77001110004','Babysitter','pass4'),
('ali5@mail.com','Ali','Zhaksylykov','Astana','+77001110005','Elderly Care specialist','pass5'),
('mira6@mail.com','Mira','Tulegenova','Almaty','+77001110006','Babysitter','pass6'),
('serik7@mail.com','Serik','Khan','Astana','+77001110007','Playmate','pass7'),
('lola8@mail.com','Lola','Iskakova','Karaganda','+77001110008','Babysitter','pass8'),
('askar9@mail.com','Askar','Omarov','Astana','+77001110009','Elderly caregiver','pass9'),
('zhanna10@mail.com','Zhanna','Mukhametova','Almaty','+77001110010','Babysitter','pass10'),

('amina11@mail.com','Amina','Aminova','Astana','+77001110011','Family member','pass11'),
('raushan12@mail.com','Raushan','Sultangali','Astana','+77001110012','Family member','pass12'),
('kairat13@mail.com','Kairat','Bekturov','Astana','+77001110013','Family member','pass13'),
('ainur14@mail.com','Ainur','Kassym','Almaty','+77001110014','Family member','pass14'),
('dias15@mail.com','Dias','Nurgali','Almaty','+77001110015','Family member','pass15'),
('aliya16@mail.com','Aliya','Kenzhe','Shymkent','+77001110016','Family member','pass16'),
('ruslan17@mail.com','Ruslan','Bek','Astana','+77001110017','Family member','pass17'),
('samal18@mail.com','Samal','Zhumagali','Karaganda','+77001110018','Family member','pass18'),
('marat19@mail.com','Marat','Yesenov','Astana','+77001110019','Family member','pass19'),
('aidana20@mail.com','Aidana','Tursyn','Almaty','+77001110020','Family member','pass20');
         
-- -caregivers        
INSERT INTO caregiver(caregiver_user_id, photo, gender, caregiving_type, hourly_rate) VALUES
(1,'photo1.jpg','Male','Babysitter',8.50),
(2,'photo2.jpg','Female','Elderly Care',12.00),
(3,'photo3.jpg','Male','Playmate',9.00),
(4,'photo4.jpg','Female','Babysitter',7.80),
(5,'photo5.jpg','Male','Elderly Care',15.00),
(6,'photo6.jpg','Female','Babysitter',10.00),
(7,'photo7.jpg','Male','Playmate',11.00),
(8,'photo8.jpg','Female','Babysitter',6.50),
(9,'photo9.jpg','Male','Elderly Care',9.50),
(10,'photo10.jpg','Female','Babysitter',13.00);
             
-- -members 
INSERT INTO member(member_user_id, house_rules, dependent_description) VALUES
(11,'No pets. Please be quiet after 9pm.','My grandmother needs elderly care.'),
(12,'No pets. Keep shoes outside.','My father needs help walking.'),
(13,'No pets. No smoking.','My mother needs daily assistance.'),
(14,'No loud music.','I have a 4-year-old son.'),
(15,'Be soft-spoken with kids.','Two children (6 and 8).'),
(16,'No pets. Hygiene is important.','Elderly aunt, 70 years old.'),
(17,'No pets. No visitors.','Grandpa after surgery.'),
(18,'No smoking.','3-year-old toddler.'),
(19,'No pets. Keep kitchen clean.','Elderly mother.'),
(20,'No loud music.','Child who likes painting.');
         
-- -Addres-
INSERT INTO address(member_user_id, house_number, street, town) VALUES
(11,'10','Tauelsizdik','Astana'),
(12,'25','Kabanbay Batyr','Astana'),
(13,'31','Kabanbay Batyr','Astana'),
(14,'5','Abay','Almaty'),
(15,'17','Satpayev','Almaty'),
(16,'9','Baitursynov','Shymkent'),
(17,'44','Saryarka','Astana'),
(18,'7','Bukhar Zhyrau','Karaganda'),
(19,'88','Turan','Astana'),
(20,'3','Al-Farabi','Almaty');

-- -Jоbs    
INSERT INTO job(member_user_id, required_caregiving_type, other_requirements, date_posted) VALUES
(11,'Elderly Care','No pets. soft-spoken caregiver preferred.','2025-10-01'),
(12,'Elderly Care','soft-spoken, experience with walkers.','2025-10-05'),
(13,'Babysitter','soft-spoken and patient.','2025-10-08'),
(14,'Babysitter','evening shifts only.','2025-10-10'),
(15,'Playmate','creative, loves drawing.','2025-10-11'),
(16,'Elderly Care','No pets. must know basic medicine.','2025-10-12'),
(17,'Babysitter','weekends only.','2025-10-15'),
(18,'Babysitter','No smoking.','2025-10-16'),
(19,'Elderly Care','No pets. soft-spoken.','2025-10-18'),
(20,'Babysitter','likes outdoor activities.','2025-10-20'),
(11,'Babysitter','short-term help, soft-spoken.','2025-10-22'),
(14,'Playmate','English speaking preferred.','2025-10-25');
            
-- -Job applications       
INSERT INTO job_application(caregiver_user_id, job_id, date_applied) VALUES
(1,1,'2025-10-02'),
(2,1,'2025-10-03'),
(5,1,'2025-10-04'),
(9,2,'2025-10-06'),
(2,2,'2025-10-06'),
(4,3,'2025-10-09'),
(6,4,'2025-10-11'),
(8,4,'2025-10-12'),
(10,7,'2025-10-16'),
(1,8,'2025-10-17'),
(6,10,'2025-10-21'),
(3,5,'2025-10-12'),
(7,12,'2025-10-26'),
(8,11,'2025-10-23');

-- -Appointments   
INSERT INTO appointment(caregiver_user_id, member_user_id, appointment_date, appointment_time, work_hours, status) VALUES
(1,14,'2025-10-12','10:00',3,'Accepted'),
(4,18,'2025-10-17','09:00',4,'Accepted'),
(6,20,'2025-10-22','12:00',2,'Accepted'),
(8,15,'2025-10-23','14:00',5,'Pending'),
(10,17,'2025-10-24','11:00',3,'Accepted'),
(2,11,'2025-10-13','09:30',6,'Accepted'),
(5,12,'2025-10-19','15:00',2,'Declined'),
(9,19,'2025-10-20','08:00',4,'Accepted'),
(3,16,'2025-10-21','16:00',3,'Accepted'),
(7,13,'2025-10-25','10:00',2,'Pending'),
(2,17,'2025-10-26','13:00',5,'Accepted');
