-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 30, 2021 at 11:03 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask-blog-site`
--

-- --------------------------------------------------------

--
-- Table structure for table `create-accounts`
--

CREATE TABLE `create-accounts` (
  `serial_no` int(11) NOT NULL,
  `name` varchar(15) NOT NULL,
  `last_name` varchar(15) NOT NULL,
  `email` varchar(20) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `create-accounts`
--

INSERT INTO `create-accounts` (`serial_no`, `name`, `last_name`, `email`, `password`) VALUES
(80, 'Star', 'Anonymus', 'star@anonymus.com', 'THis si pass');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `post_sno` int(11) NOT NULL,
  `slug` varchar(15) NOT NULL,
  `title` varchar(20) NOT NULL,
  `content` varchar(1000) NOT NULL,
  `auther` varchar(15) NOT NULL,
  `dt` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`post_sno`, `slug`, `title`, `content`, `auther`, `dt`) VALUES
(1, 'how-to-learn-py', 'Python learning ', 'Python is easy and simple programing language in the world. Python have a grate and huge community.Lorem ipsum dolor sit amet consectetur adipisicing elit. Alias nulla, nam est sit fugit optio commodi? Quidem dolore ratione aliquam alias laboriosam sed blanditiis voluptatum nam dolorem ipsum. Esse vitae natus magni error quisquam labore numquam quam ea accusamus modi! A, doloribus minima provident fugit deserunt amet consequatur reprehenderit recusandae cumque dolorem incidunt eum iusto ullam ad, eveniet perspiciatis voluptate suscipit eius nesciunt. Expedita, officia molestiae eos illo temporibus eaque fuga velit minima ducimus impedit, cupiditate laborum porro illum cumque facere! Obcaecati quas quae hic, qui pariatur natus Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta necessitatibus distinctio nostrum cum quae asperiores nesciunt deleniti eaque beatae ad. Placeat nostrum iusto odit sunt pariatur ut nihil et animi, soluta officiis dolor quis. Dolorum, adipisci nihil', 'Nawaz', ''),
(2, 'git-hub-blog', 'Github', 'Lets learn about git and github together. so make sure you konw about codingLorLorem ipsum dolor sit amet consectetur adipisicing elit. Alias nulla, nam est sit fugit optio commodi? Quidem dolore ratione aliquam alias laboriosam sed blanditiis voluptatum nam dolorem ipsum. Esse vitae natus magni error quisquam labore numquam quam ea accusamus modi! A, doloribus minima provident fugit deserunt amet consequatur reprehenderit recusandae cumque dolorem incidunt eum iusto ullam ad, eveniet perspiciatis voluptate suscipit eius nesciunt. Expedita, officia molestiae eos illo temporibus eaque fuga velit minima ducimus impedit, cupiditate laborum porro illum cumque facere! Obcaecati quas quae hic, qui pariatur natus Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta necessitatibus distinctio nostrum cum quae asperiores nesciunt deleniti eaque beatae ad. Placeat nostrum iusto odit sunt pariatur ut nihil et animi, soluta officiis dolor quis. Dolorum, adipisci nihil fugit dolorem totam', 'Asghar', ''),
(3, 'java-blog', 'Learn JAVA', 'Java is one of the bad programming language in the world.Lorem ipsum dolor sit amet consectetur adipLorem ipsum dolor sit amet consectetur adipisicing elit. Alias nulla, nam est sit fugit optio commodi? Quidem dolore ratione aliquam alias laboriosam sed blanditiis voluptatum nam dolorem ipsum. Esse vitae natus magni error quisquam labore numquam quam ea accusamus modi! A, doloribus minima provident fugit deserunt amet consequatur reprehenderit recusandae cumque dolorem incidunt eum iusto ullam ad, eveniet perspiciatis voluptate suscipit eius nesciunt. Expedita, officia molestiae eos illo temporibus eaque fuga velit minima ducimus impedit, cupiditate laborum porro illum cumque facere! Obcaecati quas quae hic, qui pariatur natus Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta necessitatibus distinctio nostrum cum quae asperiores nesciunt deleniti eaque beatae ad. Placeat nostrum iusto odit sunt pariatur ut nihil et animi, soluta officiis dolor quis. Dolorum, adipisci nihi', 'Mujahid', ''),
(4, 'ml-blog', 'Learn ML', 'To lean ML you will get alots of mony but you will loss your heir and bring and rest of your life,LoLorem ipsum dolor sit amet consectetur adipisicing elit. Alias nulla, nam est sit fugit optio commodi? Quidem dolore ratione aliquam alias laboriosam sed blanditiis voluptatum nam dolorem ipsum. Esse vitae natus magni error quisquam labore numquam quam ea accusamus modi! A, doloribus minima provident fugit deserunt amet consequatur reprehenderit recusandae cumque dolorem incidunt eum iusto ullam ad, eveniet perspiciatis voluptate suscipit eius nesciunt. Expedita, officia molestiae eos illo temporibus eaque fuga velit minima ducimus impedit, cupiditate laborum porro illum cumque facere! Obcaecati quas quae hic, qui pariatur natus Lorem ipsum dolor sit amet consectetur adipisicing elit. Soluta necessitatibus distinctio nostrum cum quae asperiores nesciunt deleniti eaque beatae ad. Placeat nostrum iusto odit sunt pariatur ut nihil et animi, soluta officiis dolor quis. Dolorum, adipisci nihi', 'Kahii', ''),
(5, 'chick-post', 'godboy ', 'i just want ot chak t he datga afjaf alfs', 'haris', '28 Jan 21'),
(7, 'tgest-ts', 'Agin testing', 'No CONTENT abilaboe the abialb to grwo and reproduce is called boi', 'Zia', '28 Jan 21');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `create-accounts`
--
ALTER TABLE `create-accounts`
  ADD PRIMARY KEY (`serial_no`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`post_sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `create-accounts`
--
ALTER TABLE `create-accounts`
  MODIFY `serial_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `post_sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
