mysqldump -u root -p --databases sdc > sdc.sql

alter table filter_el add column user_post varchar(500) after message;

create table fb_filter_assessment(id int auto_increment, meesage text, user_post varchar(2000), filter_status varchar(10), agree_value varchar(10), create_date datetime, primary key(id));

create table training_data(id int auto_increment, user_id varchar(200), 
post_id varchar(200), poster_name varchar(1000), cred_value varchar(10), likes int, shares int,
comments int, hashtags int, images int, vdo int, url int, wot_score int, word_in_dict int,
word_outside_dict int, num_of_number_in_sentense int, app_sender int, share_with_location int, share_with_non_location int, tag_with int, 
feeling_status int, share_public int, share_only_friend int, 
word_count int, character_length int, question_mark int, exclamation_mark int, day_pass int,
create_date datetime, message text,
primary key(id));