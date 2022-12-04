-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 13, 2022 at 11:29 PM
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
-- Database: `car_pooling`
--

-- --------------------------------------------------------

--
-- Table structure for table `autista`
--

CREATE TABLE `autista` (
  `id_autista` int(11) NOT NULL,
  `nome` varchar(20) NOT NULL,
  `cognome` varchar(20) NOT NULL,
  `data_nascita` date NOT NULL,
  `sesso` varchar(10) NOT NULL,
  `num_patente` varchar(10) NOT NULL,
  `scad_patente` date NOT NULL,
  `num_telefono` varchar(15) NOT NULL,
  `dati_auto` varchar(10) DEFAULT NULL,
  `email` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `autista`
--

INSERT INTO `autista` (`id_autista`, `nome`, `cognome`, `data_nascita`, `sesso`, `num_patente`, `scad_patente`, `num_telefono`, `dati_auto`, `email`) VALUES
(1, 'TESSY', 'ASTORINO', '1982-02-23', 'F', 'vhfdb23', '2022-02-28', '+3915156118', 'bvfduibv', 'autista1@gmail.com'),
(2, 'ROMANA', 'FIORA', '1976-02-12', 'F', 'huyvb43', '2022-03-16', '+39165184', 'fdsvfdv', 'autista2@gmail.com'),
(3, 'CARLA', 'DURMISHAJ', '1974-02-13', 'F', 'vbfgb158', '2022-02-09', '+39511182', 'hvdfbvvh', 'autista3@gmail.com'),
(4, 'YANISS', 'SRIJ', '1974-04-17', 'M', 'jkvnf34', '2022-05-10', '+395189181', 'vidfbid', 'autista4@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `automobile`
--

CREATE TABLE `automobile` (
  `codice_auto` varchar(10) NOT NULL,
  `targa` varchar(10) NOT NULL,
  `num_posti` int(11) NOT NULL,
  `marca` varchar(15) NOT NULL,
  `modello` varchar(15) NOT NULL,
  `colore` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `automobile`
--

INSERT INTO `automobile` (`codice_auto`, `targa`, `num_posti`, `marca`, `modello`, `colore`) VALUES
('bvfduibv', 'ivbfd1', 4, 'opel', 'agila', 'gialla'),
('cdsc', 'cd', 0, 'cds', 'cds', 'cd'),
('fdsvfdv', 'vfdvdvfd', 5, 'fiat', 'doblo', 'rosso'),
('hvdfbvvh', 'cvsbdvu', 4, 'ferrari', 'turbo', 'rosso'),
('vidfbid', 'vbdfvb', 2, 'maserati', 'giannina', 'rosso');

-- --------------------------------------------------------

--
-- Table structure for table `feedback_autista`
--

CREATE TABLE `feedback_autista` (
  `id_feedback` int(11) NOT NULL,
  `cf` varchar(16) NOT NULL,
  `id_autista` int(11) NOT NULL,
  `valutazione` float NOT NULL COMMENT 'valutazione => Da 1 a 5, incremento di 0.5',
  `feedback` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `feedback_autista`
--

INSERT INTO `feedback_autista` (`id_feedback`, `cf`, `id_autista`, `valutazione`, `feedback`) VALUES
(1, 'BLOVTR67T42A314G', 1, 3.5, ''),
(2, 'DRJNMR13L53B195F', 2, 4, '');

-- --------------------------------------------------------

--
-- Table structure for table `feedback_passeggero`
--

CREATE TABLE `feedback_passeggero` (
  `id_feedback` int(11) NOT NULL,
  `id_autista` int(11) NOT NULL,
  `cf` varchar(16) NOT NULL,
  `valutazione` float NOT NULL COMMENT 'valutazione => Da 1 a 5, incremento di 0.5',
  `feedback` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `feedback_passeggero`
--

INSERT INTO `feedback_passeggero` (`id_feedback`, `id_autista`, `cf`, `valutazione`, `feedback`) VALUES
(1, 1, 'BLOVTR67T42A314G', 3, NULL),
(2, 2, 'BLOVTR67T42A314G', 4, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `passeggero`
--

CREATE TABLE `passeggero` (
  `cf` varchar(16) NOT NULL,
  `nome` varchar(20) NOT NULL,
  `cognome` varchar(20) NOT NULL,
  `num_telefono` varchar(15) NOT NULL,
  `codice_documento` varchar(10) NOT NULL,
  `email` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `passeggero`
--

INSERT INTO `passeggero` (`cf`, `nome`, `cognome`, `num_telefono`, `codice_documento`, `email`) VALUES
('BLOVTR67T42A314G', 'Vittoria', 'bouali', '+393568438514', 'cibds34', 'prova@gmail.com'),
('DRJNMR13L53B195F', 'Annamaria', 'De Araujo', '+39685151651', 'cbfdsc3', 'prova@gmail.com'),
('GBTMJN16E30H577J', 'Marjan', 'Gabutti', '+3915616814', 'cbdsic23', 'prova@gmail.com'),
('HJAHCN77P13L573V', 'Hacen', 'Hajoui', '+391651681', 'vcudfi21', 'prova@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `prenotazione`
--

CREATE TABLE `prenotazione` (
  `codice` int(11) NOT NULL,
  `id_viaggio` int(11) NOT NULL,
  `cf` varchar(16) NOT NULL,
  `risposta` enum('Il viaggio è stato prenotato','Il viaggio non è stato prenotato') DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `prenotazione`
--

INSERT INTO `prenotazione` (`codice`, `id_viaggio`, `cf`, `risposta`) VALUES
(15, 1, 'BLOVTR67T42A314G', 'Il viaggio non è stato prenotato');

-- --------------------------------------------------------

--
-- Table structure for table `viaggio`
--

CREATE TABLE `viaggio` (
  `id_viaggio` int(11) NOT NULL,
  `id_autista` int(11) NOT NULL,
  `data_partenza` date NOT NULL,
  `ora_partenza` time NOT NULL,
  `citta_partenza` varchar(20) NOT NULL,
  `citta_destinazione` varchar(20) NOT NULL,
  `durata_viaggio` time NOT NULL,
  `prezzo_passeggero` float NOT NULL,
  `prenotazione` enum('0','1') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `viaggio`
--

INSERT INTO `viaggio` (`id_viaggio`, `id_autista`, `data_partenza`, `ora_partenza`, `citta_partenza`, `citta_destinazione`, `durata_viaggio`, `prezzo_passeggero`, `prenotazione`) VALUES
(1, 1, '2022-02-24', '18:44:26', 'Milano', 'Roma', '06:44:26', 15, '1'),
(2, 2, '2022-02-10', '07:44:26', 'Milano', 'Roma', '13:44:26', 15, '1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `autista`
--
ALTER TABLE `autista`
  ADD PRIMARY KEY (`id_autista`),
  ADD KEY `dati_auto` (`dati_auto`);

--
-- Indexes for table `automobile`
--
ALTER TABLE `automobile`
  ADD PRIMARY KEY (`codice_auto`);

--
-- Indexes for table `feedback_autista`
--
ALTER TABLE `feedback_autista`
  ADD PRIMARY KEY (`id_feedback`),
  ADD KEY `cf` (`cf`),
  ADD KEY `id_autista` (`id_autista`);

--
-- Indexes for table `feedback_passeggero`
--
ALTER TABLE `feedback_passeggero`
  ADD PRIMARY KEY (`id_feedback`),
  ADD KEY `id_autista` (`id_autista`),
  ADD KEY `cf` (`cf`);

--
-- Indexes for table `passeggero`
--
ALTER TABLE `passeggero`
  ADD PRIMARY KEY (`cf`);

--
-- Indexes for table `prenotazione`
--
ALTER TABLE `prenotazione`
  ADD PRIMARY KEY (`codice`),
  ADD KEY `id_viaggio` (`id_viaggio`),
  ADD KEY `cf` (`cf`),
  ADD KEY `id_viaggio_2` (`id_viaggio`);

--
-- Indexes for table `viaggio`
--
ALTER TABLE `viaggio`
  ADD PRIMARY KEY (`id_viaggio`),
  ADD KEY `id_autista` (`id_autista`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `autista`
--
ALTER TABLE `autista`
  MODIFY `id_autista` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `feedback_autista`
--
ALTER TABLE `feedback_autista`
  MODIFY `id_feedback` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `feedback_passeggero`
--
ALTER TABLE `feedback_passeggero`
  MODIFY `id_feedback` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `prenotazione`
--
ALTER TABLE `prenotazione`
  MODIFY `codice` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `viaggio`
--
ALTER TABLE `viaggio`
  MODIFY `id_viaggio` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `autista`
--
ALTER TABLE `autista`
  ADD CONSTRAINT `autista_ibfk_1` FOREIGN KEY (`dati_auto`) REFERENCES `automobile` (`codice_auto`);

--
-- Constraints for table `feedback_autista`
--
ALTER TABLE `feedback_autista`
  ADD CONSTRAINT `feedback_autista_ibfk_2` FOREIGN KEY (`id_autista`) REFERENCES `autista` (`id_autista`),
  ADD CONSTRAINT `feedback_autista_ibfk_3` FOREIGN KEY (`cf`) REFERENCES `passeggero` (`cf`);

--
-- Constraints for table `feedback_passeggero`
--
ALTER TABLE `feedback_passeggero`
  ADD CONSTRAINT `feedback_passeggero_ibfk_3` FOREIGN KEY (`id_autista`) REFERENCES `autista` (`id_autista`),
  ADD CONSTRAINT `feedback_passeggero_ibfk_4` FOREIGN KEY (`cf`) REFERENCES `passeggero` (`cf`);

--
-- Constraints for table `prenotazione`
--
ALTER TABLE `prenotazione`
  ADD CONSTRAINT `prenotazione_ibfk_1` FOREIGN KEY (`cf`) REFERENCES `passeggero` (`cf`),
  ADD CONSTRAINT `prenotazione_ibfk_2` FOREIGN KEY (`id_viaggio`) REFERENCES `viaggio` (`id_viaggio`);

--
-- Constraints for table `viaggio`
--
ALTER TABLE `viaggio`
  ADD CONSTRAINT `viaggio_ibfk_1` FOREIGN KEY (`id_autista`) REFERENCES `autista` (`id_autista`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
