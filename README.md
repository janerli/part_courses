-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema courses
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema courses
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `courses` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `courses` ;

-- -----------------------------------------------------
-- Table `courses`.`roles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `courses`.`roles` (
  `role_id` INT NOT NULL AUTO_INCREMENT,
  `role_name` VARCHAR(50) NULL DEFAULT NULL,
  PRIMARY KEY (`role_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `courses`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `courses`.`users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(100) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `role_id` INT NULL DEFAULT NULL,
  `full_name` VARCHAR(150) NULL DEFAULT NULL,
  `email` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  INDEX `role_id` (`role_id` ASC) VISIBLE,
  CONSTRAINT `users_ibfk_1`
    FOREIGN KEY (`role_id`)
    REFERENCES `courses`.`roles` (`role_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `courses`.`courses`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `courses`.`courses` (
  `course_id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(200) NULL DEFAULT NULL,
  `description` TEXT NULL DEFAULT NULL,
  `teacher_id` INT NULL DEFAULT NULL,
  `price` DECIMAL(10,2) NULL DEFAULT NULL,
  `created_date` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `status` VARCHAR(30) NULL DEFAULT NULL,
  PRIMARY KEY (`course_id`),
  INDEX `teacher_id` (`teacher_id` ASC) VISIBLE,
  CONSTRAINT `courses_ibfk_1`
    FOREIGN KEY (`teacher_id`)
    REFERENCES `courses`.`users` (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `courses`.`enrollments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `courses`.`enrollments` (
  `enrollment_id` INT NOT NULL AUTO_INCREMENT,
  `student_id` INT NULL DEFAULT NULL,
  `course_id` INT NULL DEFAULT NULL,
  `enrollment_date` DATETIME NULL DEFAULT NULL,
  `status` VARCHAR(30) NULL DEFAULT NULL,
  PRIMARY KEY (`enrollment_id`),
  INDEX `student_id` (`student_id` ASC) VISIBLE,
  INDEX `course_id` (`course_id` ASC) VISIBLE,
  CONSTRAINT `enrollments_ibfk_1`
    FOREIGN KEY (`student_id`)
    REFERENCES `courses`.`users` (`user_id`),
  CONSTRAINT `enrollments_ibfk_2`
    FOREIGN KEY (`course_id`)
    REFERENCES `courses`.`courses` (`course_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `courses`.`lessons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `courses`.`lessons` (
  `lesson_id` INT NOT NULL AUTO_INCREMENT,
  `course_id` INT NULL DEFAULT NULL,
  `title` VARCHAR(200) NULL DEFAULT NULL,
  `content` TEXT NULL DEFAULT NULL,
  `video_url` VARCHAR(500) NULL DEFAULT NULL,
  `duration_minutes` INT NULL DEFAULT NULL,
  `order_number` INT NULL DEFAULT NULL,
  PRIMARY KEY (`lesson_id`),
  INDEX `course_id` (`course_id` ASC) VISIBLE,
  CONSTRAINT `lessons_ibfk_1`
    FOREIGN KEY (`course_id`)
    REFERENCES `courses`.`courses` (`course_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `courses`.`homeworks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `courses`.`homeworks` (
  `homework_id` INT NOT NULL AUTO_INCREMENT,
  `lesson_id` INT NULL DEFAULT NULL,
  `student_id` INT NULL DEFAULT NULL,
  `task_text` TEXT NULL DEFAULT NULL,
  `answer_text` TEXT NULL DEFAULT NULL,
  `score` INT NULL DEFAULT NULL,
  `status` VARCHAR(30) NULL DEFAULT NULL,
  `submitted_date` DATETIME NULL DEFAULT NULL,
  `reviewed_date` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`homework_id`),
  INDEX `lesson_id` (`lesson_id` ASC) VISIBLE,
  INDEX `student_id` (`student_id` ASC) VISIBLE,
  CONSTRAINT `homeworks_ibfk_1`
    FOREIGN KEY (`lesson_id`)
    REFERENCES `courses`.`lessons` (`lesson_id`),
  CONSTRAINT `homeworks_ibfk_2`
    FOREIGN KEY (`student_id`)
    REFERENCES `courses`.`users` (`user_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
