INSERT INTO public.auth_permission (name,content_type_id,codename) VALUES
	 ('Can add log entry',1,'add_logentry'),
	 ('Can change log entry',1,'change_logentry'),
	 ('Can delete log entry',1,'delete_logentry'),
	 ('Can view log entry',1,'view_logentry'),
	 ('Can add permission',2,'add_permission'),
	 ('Can change permission',2,'change_permission'),
	 ('Can delete permission',2,'delete_permission'),
	 ('Can view permission',2,'view_permission'),
	 ('Can add group',3,'add_group'),
	 ('Can change group',3,'change_group');
INSERT INTO public.auth_permission (name,content_type_id,codename) VALUES
	 ('Can delete group',3,'delete_group'),
	 ('Can view group',3,'view_group'),
	 ('Can add user',4,'add_user'),
	 ('Can change user',4,'change_user'),
	 ('Can delete user',4,'delete_user'),
	 ('Can view user',4,'view_user'),
	 ('Can add content type',5,'add_contenttype'),
	 ('Can change content type',5,'change_contenttype'),
	 ('Can delete content type',5,'delete_contenttype'),
	 ('Can view content type',5,'view_contenttype');
INSERT INTO public.auth_permission (name,content_type_id,codename) VALUES
	 ('Can add session',6,'add_session'),
	 ('Can change session',6,'change_session'),
	 ('Can delete session',6,'delete_session'),
	 ('Can view session',6,'view_session'),
	 ('Can add extra',7,'add_extra'),
	 ('Can change extra',7,'change_extra'),
	 ('Can delete extra',7,'delete_extra'),
	 ('Can view extra',7,'view_extra'),
	 ('Can add departamento',8,'add_departamento'),
	 ('Can change departamento',8,'change_departamento');
INSERT INTO public.auth_permission (name,content_type_id,codename) VALUES
	 ('Can delete departamento',8,'delete_departamento'),
	 ('Can view departamento',8,'view_departamento');
INSERT INTO public.auth_user ("password",last_login,is_superuser,username,first_name,last_name,email,is_staff,is_active,date_joined) VALUES
	 ('pbkdf2_sha256$870000$KTZJxBV4Om1xWd204PABny$QDd4fhwOvM0QGwEH/2pvMKzE4R0Dcve2czOUosAvZHs=','2024-08-26 23:25:00.689411-04',false,'user2','','','user2@mail.com',false,true,'2024-08-26 23:23:39.556912-04'),
	 ('pbkdf2_sha256$870000$4KpjkJoVXlZ4MLdM0wIuxz$66K0cykwOodjJtrowLqXela36UHtsTYWPJEgROEg/J0=','2024-08-27 01:14:38.312775-04',false,'user3','','','user3@mail.com',false,true,'2024-08-27 01:14:37.083225-04'),
	 ('pbkdf2_sha256$870000$9sgIqiB633lSnSHVTiDKuh$I8DDF7ICbQzyUxNhQSdAAfUq63rmNCYLFLF8CYBi0+Q=','2024-08-27 01:14:54.261152-04',false,'user1','','','user1@mail.com',false,true,'2024-08-26 21:23:53.112341-04'),
	 ('pbkdf2_sha256$870000$lE5rdBpVo5KSWEeDqFUS0X$6cqxJL0YH7Zgicy+Fckv3ardvxm76a7E3WweFM6WXl0=','2024-08-27 01:15:58.895902-04',true,'admin','','','admin@mail.com',true,true,'2024-08-26 20:26:52.393297-04');
INSERT INTO public.django_content_type (app_label,model) VALUES
	 ('admin','logentry'),
	 ('auth','permission'),
	 ('auth','group'),
	 ('auth','user'),
	 ('contenttypes','contenttype'),
	 ('sessions','session'),
	 ('web','extra'),
	 ('web','departamento');
INSERT INTO public.django_migrations (app,name,applied) VALUES
	 ('contenttypes','0001_initial','2024-08-26 20:26:26.705174-04'),
	 ('auth','0001_initial','2024-08-26 20:26:26.783335-04'),
	 ('admin','0001_initial','2024-08-26 20:26:26.805783-04'),
	 ('admin','0002_logentry_remove_auto_add','2024-08-26 20:26:26.818473-04'),
	 ('admin','0003_logentry_add_action_flag_choices','2024-08-26 20:26:26.847367-04'),
	 ('contenttypes','0002_remove_content_type_name','2024-08-26 20:26:26.867862-04'),
	 ('auth','0002_alter_permission_name_max_length','2024-08-26 20:26:26.880551-04'),
	 ('auth','0003_alter_user_email_max_length','2024-08-26 20:26:26.895193-04'),
	 ('auth','0004_alter_user_username_opts','2024-08-26 20:26:26.904952-04'),
	 ('auth','0005_alter_user_last_login_null','2024-08-26 20:26:26.915686-04');
INSERT INTO public.django_migrations (app,name,applied) VALUES
	 ('auth','0006_require_contenttypes_0002','2024-08-26 20:26:26.917639-04'),
	 ('auth','0007_alter_validators_add_error_messages','2024-08-26 20:26:26.9274-04'),
	 ('auth','0008_alter_user_username_max_length','2024-08-26 20:26:26.945943-04'),
	 ('auth','0009_alter_user_last_name_max_length','2024-08-26 20:26:26.958638-04'),
	 ('auth','0010_alter_group_name_max_length','2024-08-26 20:26:26.972294-04'),
	 ('auth','0011_update_proxy_permissions','2024-08-26 20:26:26.981078-04'),
	 ('auth','0012_alter_user_first_name_max_length','2024-08-26 20:26:26.994743-04'),
	 ('sessions','0001_initial','2024-08-26 20:26:27.007431-04'),
	 ('web','0001_initial','2024-08-26 20:26:27.042567-04'),
	 ('web','0002_alter_departamento_extras','2024-08-27 00:39:57.494796-04');
INSERT INTO public.django_session (session_key,session_data,expire_date) VALUES
	 ('xjp50snzou67xu90c9ualmf6voqgto0p','.eJxVjEEOwiAQRe_C2hCGDh3q0r1nINOBStVAUtqV8e7apAvd_vfef6nA25rD1tIS5qjOCtTpdxtZHqnsIN653KqWWtZlHvWu6IM2fa0xPS-H-3eQueVvTQTYS-qMHRLIZCYxXgg7EUQCN6BlgtgZj66PwsCRXPJWDJAAoaj3B8jWNzQ:1sioYg:S7Nu38lvCDRQ3yml-DQH0ZGd3oWQ5DmtvcFEjiW1SNI','2024-09-10 02:15:58.898831-03');
INSERT INTO public.web_departamento (numero,metros_2,user_id) VALUES
	 ('505',100,2),
	 ('705',50,3),
	 ('306',70,2),
	 ('904',120,2),
	 ('801',120,2);
INSERT INTO public.web_departamento_extras (departamento_id,extra_id) VALUES
	 (2,1),
	 (3,1),
	 (1,5),
	 (4,1),
	 (4,2),
	 (4,5),
	 (5,1),
	 (5,5),
	 (4,6);
INSERT INTO public.web_extra (nombre,porcentaje) VALUES
	 ('Estacionamiento',0.15),
	 ('Balcon',0.1),
	 ('Bodega',0.2),
	 ('Calefacción',0.25);
