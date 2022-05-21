-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: May 21, 2022 at 05:01 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tubes`
--

-- --------------------------------------------------------

--
-- Table structure for table `penerbangan`
--

CREATE TABLE `penerbangan` (
  `id` int(11) NOT NULL,
  `no_penerbangan` varchar(20) NOT NULL,
  `asal` varchar(20) NOT NULL,
  `tujuan` varchar(20) NOT NULL,
  `date_berangkat` varchar(20) NOT NULL,
  `time_berangkat` varchar(10) NOT NULL,
  `time_datang` varchar(10) NOT NULL,
  `maskapai` varchar(10) NOT NULL,
  `harga` varchar(10) NOT NULL,
  `kursi` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `penerbangan`
--

INSERT INTO `penerbangan` (`id`, `no_penerbangan`, `asal`, `tujuan`, `date_berangkat`, `time_berangkat`, `time_datang`, `maskapai`, `harga`, `kursi`) VALUES
(1, 'JT 0534', 'Balikpapan', 'Jakarta', '01 Januari 2022', '10:20', '11:10', 'Lion Air', '1397100', '72'),
(2, 'JT 0617', 'Balikpapan', 'Yogyakarta', '01 Januari 2022', '08:05', '13:40', 'Lion Air', '1650000', '72'),
(3, 'ID 6531', 'Yogyakarta', 'Balikpapan', '02 Januari 2022', '07:00', '09:00', 'Batik Air', '1300000', '65'),
(4, 'JT 0889', 'Jakarta', 'Balikpapan', '02 Januari 2022', '15:30', '17:00', 'Lion Air', '1050000', '65'),
(5, 'QG 5510', 'Balikpapan', 'Bali', '02 Januari 2022', '12:00', '13:40', 'Citilink', '1200000', '45'),
(6, 'QG 2212', 'Balikpapan', 'Bali', '02 Januari 2022', '13:00', '14:40', 'Citilink', '1100000', '45'),
(7, 'ID 5517', 'Jakarta', 'Bali', '02 Januari 2022', '07:30', '08:40', 'Batik Air', '850000', '61'),
(8, 'ID 0817', 'Jakarta', 'Balikpapan', '03 Januari 2022', '09:00', '10:30', 'Batik Air', '1300000', '46'),
(9, 'QG 1221', 'Balikpapan', 'Surabaya', '03 Januari 2022', '07:00', '09:00', 'Citilink', '989000', '32'),
(10, 'QG 0677', 'Surabaya', 'Jakarta', '03 Januari 2022', '08:30', '09:45', 'Citilink', '550000', '50'),
(27, 'JT-301', 'Nias', 'Jakarta', '04 Januari 2021', '06:30', '09:30', 'Lion Air', '1035500', '54'),
(29, 'QG 439', 'Balikpapan', 'Nias', '04 Januari 2022', '16:50', '19:30', 'Citilink', '1570349', '34'),
(30, 'IW 1265', 'Nias', 'Balikpapan', '04 Januari 2022', '06:30', '09:30', 'Wings Air', '1469900', '54'),
(31, 'GA 7117', 'Nias', 'Bali', '05 Januari 2021', '12:50', '17:30', 'Garuda', '2286135', '51');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `penerbangan`
--
ALTER TABLE `penerbangan`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `penerbangan`
--
ALTER TABLE `penerbangan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
