-- phpMyAdmin SQL Dump
-- version 4.0.4
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Dec 14, 2023 at 01:39 PM
-- Server version: 5.6.12-log
-- PHP Version: 5.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `conductor`
--
CREATE DATABASE IF NOT EXISTS `conductor` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `conductor`;

-- --------------------------------------------------------

--
-- Table structure for table `app_integration_application_register`
--

CREATE TABLE IF NOT EXISTS `app_integration_application_register` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `password` varchar(100) NOT NULL,
  `app_admin_lg` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `app_integration_application_register`
--

INSERT INTO `app_integration_application_register` (`id`, `username`, `designation`, `email`, `phone`, `password`, `app_admin_lg`) VALUES
(1, 'Vinoth', 'Material Supervisor', 'vinoth@gmail.com', '9685748574', '1234', 1);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=49 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add client', 7, 'add_client'),
(26, 'Can change client', 7, 'change_client'),
(27, 'Can delete client', 7, 'delete_client'),
(28, 'Can view client', 7, 'view_client'),
(29, 'Can add client_details', 8, 'add_client_details'),
(30, 'Can change client_details', 8, 'change_client_details'),
(31, 'Can delete client_details', 8, 'delete_client_details'),
(32, 'Can view client_details', 8, 'view_client_details'),
(33, 'Can add client_register', 9, 'add_client_register'),
(34, 'Can change client_register', 9, 'change_client_register'),
(35, 'Can delete client_register', 9, 'delete_client_register'),
(36, 'Can view client_register', 9, 'view_client_register'),
(37, 'Can add manganese_register', 10, 'add_manganese_register'),
(38, 'Can change manganese_register', 10, 'change_manganese_register'),
(39, 'Can delete manganese_register', 10, 'delete_manganese_register'),
(40, 'Can view manganese_register', 10, 'view_manganese_register'),
(41, 'Can add application_register', 11, 'add_application_register'),
(42, 'Can change application_register', 11, 'change_application_register'),
(43, 'Can delete application_register', 11, 'delete_application_register'),
(44, 'Can view application_register', 11, 'view_application_register'),
(45, 'Can add porosity_register', 12, 'add_porosity_register'),
(46, 'Can change porosity_register', 12, 'change_porosity_register'),
(47, 'Can delete porosity_register', 12, 'delete_porosity_register'),
(48, 'Can view porosity_register', 12, 'view_porosity_register');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `clients_client`
--

CREATE TABLE IF NOT EXISTS `clients_client` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `client_client_register`
--

CREATE TABLE IF NOT EXISTS `client_client_register` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `location` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `password` varchar(100) NOT NULL,
  `cl_admin_lg` tinyint(1) NOT NULL,
  `consumer_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `consumer_id` (`consumer_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `client_client_register`
--

INSERT INTO `client_client_register` (`id`, `username`, `location`, `email`, `phone`, `password`, `cl_admin_lg`, `consumer_id`) VALUES
(1, 'sivaraman', 'Chennai', 'siva@gmail.com', '9638527412', '1234', 1, 'CLI-1248'),
(3, 'kumar', 'Tirchy', 'kumar@gmail.com', '7418529632', '1234', 1, 'CLI-1934');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(11, 'App_Integration', 'application_register'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(9, 'Client', 'client_register'),
(7, 'Clients', 'client'),
(8, 'Clients', 'client_details'),
(5, 'contenttypes', 'contenttype'),
(10, 'Manganese_Process', 'manganese_register'),
(12, 'Porosity_Analysis', 'porosity_register'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=27 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'Clients', '0001_initial', '2023-12-12 06:56:42.008502'),
(2, 'contenttypes', '0001_initial', '2023-12-12 06:56:42.511894'),
(3, 'auth', '0001_initial', '2023-12-12 06:56:49.452367'),
(4, 'admin', '0001_initial', '2023-12-12 06:56:50.646356'),
(5, 'admin', '0002_logentry_remove_auto_add', '2023-12-12 06:56:50.690340'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2023-12-12 06:56:50.720366'),
(7, 'contenttypes', '0002_remove_content_type_name', '2023-12-12 06:56:51.997372'),
(8, 'auth', '0002_alter_permission_name_max_length', '2023-12-12 06:56:52.460736'),
(9, 'auth', '0003_alter_user_email_max_length', '2023-12-12 06:56:52.961181'),
(10, 'auth', '0004_alter_user_username_opts', '2023-12-12 06:56:53.005166'),
(11, 'auth', '0005_alter_user_last_login_null', '2023-12-12 06:56:53.381511'),
(12, 'auth', '0006_require_contenttypes_0002', '2023-12-12 06:56:53.412481'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2023-12-12 06:56:53.448513'),
(14, 'auth', '0008_alter_user_username_max_length', '2023-12-12 06:56:53.872845'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2023-12-12 06:56:54.380245'),
(16, 'auth', '0010_alter_group_name_max_length', '2023-12-12 06:56:55.118829'),
(17, 'auth', '0011_update_proxy_permissions', '2023-12-12 06:56:55.164866'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2023-12-12 06:56:55.876437'),
(19, 'sessions', '0001_initial', '2023-12-12 06:56:56.329834'),
(20, 'Client', '0001_initial', '2023-12-12 07:25:17.263079'),
(21, 'Client', '0002_client_register_cl_admin_lg', '2023-12-12 08:48:57.659356'),
(22, 'Manganese_Process', '0001_initial', '2023-12-12 09:37:20.986079'),
(23, 'Manganese_Process', '0002_rename_location_manganese_register_designation', '2023-12-12 09:52:55.367408'),
(24, 'App_Integration', '0001_initial', '2023-12-12 11:06:56.874439'),
(25, 'Porosity_Analysis', '0001_initial', '2023-12-12 12:13:24.894182'),
(26, 'Client', '0003_client_register_consumer_id', '2023-12-14 11:19:02.249723');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1kkwyihrsxtxxuic163188qi0qy2ctwz', '.eJyrVkrOyUzNK1GyUirOLEt0SM9NzMzRS87PVdJRSkzJzczLLC4pSizJLwIqAPORVNQCAJ9QFdM:1rDluG:BknJhbp_tSiVN5Vjk_pfLbgFBxt5MKTkqSg54uX1hlA', '2023-12-28 13:37:40.642283');

-- --------------------------------------------------------

--
-- Table structure for table `manganese_process_manganese_register`
--

CREATE TABLE IF NOT EXISTS `manganese_process_manganese_register` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `password` varchar(100) NOT NULL,
  `mg_admin_lg` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `manganese_process_manganese_register`
--

INSERT INTO `manganese_process_manganese_register` (`id`, `username`, `designation`, `email`, `phone`, `password`, `mg_admin_lg`) VALUES
(1, 'suresh', 'Material Head', 'suresh@gmail.com', '9638527414', '1234', 1);

-- --------------------------------------------------------

--
-- Table structure for table `porosity_analysis_porosity_register`
--

CREATE TABLE IF NOT EXISTS `porosity_analysis_porosity_register` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone` varchar(10) NOT NULL,
  `password` varchar(100) NOT NULL,
  `por_admin_lg` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `porosity_analysis_porosity_register`
--

INSERT INTO `porosity_analysis_porosity_register` (`id`, `username`, `designation`, `email`, `phone`, `password`, `por_admin_lg`) VALUES
(2, 'Naresh', 'Material Supervisor', 'naresh@gmail.com', '9638527412', '1234', 0);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
