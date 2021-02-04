/*
SQLyog Ultimate v13.1.1 (64 bit)
MySQL - 10.4.11-MariaDB : Database - db_bot_restoran
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_bot_restoran` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `db_bot_restoran`;

/*Table structure for table `tb_detail_pesanan` */

DROP TABLE IF EXISTS `tb_detail_pesanan`;

CREATE TABLE `tb_detail_pesanan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_pesanan` int(11) DEFAULT NULL,
  `id_menu` int(11) DEFAULT NULL,
  `kuantitas` int(11) DEFAULT NULL,
  `harga_satuan` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `det_pesan` (`id_pesanan`),
  KEY `det_menu` (`id_menu`),
  CONSTRAINT `det_menu` FOREIGN KEY (`id_menu`) REFERENCES `tb_menu` (`id`),
  CONSTRAINT `det_pesan` FOREIGN KEY (`id_pesanan`) REFERENCES `tb_pesanan` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_detail_pesanan` */

insert  into `tb_detail_pesanan`(`id`,`id_pesanan`,`id_menu`,`kuantitas`,`harga_satuan`,`total`) values 
(1,1,1,2,7000,14000),
(2,1,4,2,2000,4000),
(3,2,2,2,5000,10000),
(4,2,3,2,4000,8000),
(5,3,1,2,7000,14000),
(6,3,3,2,4000,8000),
(7,4,2,3,5000,15000),
(8,5,4,2,2000,4000),
(9,6,1,4,7000,28000),
(10,7,1,4,7000,28000),
(11,8,2,3,5000,15000),
(12,9,3,5,4000,20000);

/*Table structure for table `tb_inbox` */

DROP TABLE IF EXISTS `tb_inbox`;

CREATE TABLE `tb_inbox` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message_id` int(11) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `chat_id` int(11) DEFAULT NULL,
  `text` text DEFAULT NULL,
  `status_chat` int(11) DEFAULT NULL,
  `konteks` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_inbox` */

insert  into `tb_inbox`(`id`,`message_id`,`username`,`chat_id`,`text`,`status_chat`,`konteks`) values 
(1,1148,'Diatmiko',874647857,'/start',0,'mulai'),
(2,1150,'Diatmiko',874647857,'halo',0,'pembuka'),
(3,1152,'Diatmiko',874647857,'selamat pagi',0,'pembuka'),
(4,1154,'Diatmiko',874647857,'selamat malam',0,'pembuka'),
(5,1156,'Diatmiko',874647857,'hai',0,'pembuka'),
(6,1158,'Diatmiko',874647857,'saya ingin melihat daftar mnu',0,'menu'),
(7,1161,'Diatmiko',874647857,'saya ingin melihat daftar menu makanan',0,'menu'),
(8,1164,'Diatmiko',874647857,'saya infin melihat daftar mrnu minuman',0,'menu'),
(9,1167,'Diatmiko',874647857,'saya ingin memesan menu roti',0,'pesan'),
(10,1169,'Diatmiko',874647857,'saya ingin memesan roti 2 2',0,'pesan'),
(11,1171,'Diatmiko',874647857,'saya ingin memesan menu',0,'pesan'),
(12,1173,'Diatmiko',874647857,'saya ingin memesan menu roti 2',0,'pesan'),
(13,1176,'Diatmiko',874647857,'saya ingin memesan teh 2',0,'pesan'),
(14,1178,'Diatmiko',874647857,'saya ingin mengulang pesanan',6,'ulang'),
(15,1180,'Diatmiko',874647857,'ya',0,'ulang'),
(16,1182,'Diatmiko',874647857,'saya ingin memesan menu roti 2 teh 2',0,'pesan'),
(17,1185,'Diatmiko',874647857,'saya ingin melihat total pesanan saya',0,'total'),
(18,1188,'Diatmiko',874647857,'saya sudah selesai memesan',7,'selesai'),
(19,1192,'Diatmiko',874647857,'tidak',0,'selesai'),
(20,1194,'Diatmiko',874647857,'saya sudah selesai memesan',7,'selesai'),
(21,1198,'Diatmiko',874647857,'wadaw gak tuh',7,'selesai'),
(22,1201,'Diatmiko',874647857,'ya',0,'selesai'),
(23,1203,'Diatmiko',874647857,'halo',0,'pembuka'),
(24,1205,'Diatmiko',874647857,'hai',0,'pembuka'),
(25,1207,'Diatmiko',874647857,'halo',0,'pembuka'),
(26,1209,'Diatmiko',874647857,'selamat pagi',0,'pembuka'),
(27,1211,'Diatmiko',874647857,'saya ingin melihat menu makanan',0,'menu'),
(28,1214,'Diatmiko',874647857,'saya ingin melihat daftar menu minuman',0,'menu'),
(29,1217,'Diatmiko',874647857,'saya ingin memesan menu',0,'pesan'),
(30,1219,'Diatmiko',874647857,'saya ingin memesan menu roti bakar 2 dan teh 2',0,'pesan'),
(31,1222,'Diatmiko',874647857,'saya ingin mengulang pesanan',6,'ulang'),
(32,1224,'Diatmiko',874647857,'ya',0,'ulang'),
(33,1226,'Diatmiko',874647857,'saya ingin memesan kentang goreng 2 dan kopi 2',0,'pesan'),
(34,1229,'Diatmiko',874647857,'saya sudah selesai memesan',7,'selesai'),
(35,1233,'Diatmiko',874647857,'ya',0,'selesai'),
(36,1235,'Diatmiko',874647857,'hai',0,'pembuka'),
(37,1237,'Diatmiko',874647857,'saya ingin melihat dafatar menu',0,'menu'),
(38,1240,'Diatmiko',874647857,'saya mau cek list menu',0,'menu'),
(39,1243,'Diatmiko',874647857,'saya pesan menu roti 2 dan kopi 2',0,'pesan'),
(40,1246,'Diatmiko',874647857,'/start',0,'mulai'),
(41,1248,'Diatmiko',874647857,'/start',0,'mulai'),
(42,1250,'Diatmiko',874647857,'/start',0,'mulai'),
(43,1252,'Diatmiko',874647857,'hai',0,'pembuka'),
(44,1254,'Diatmiko',874647857,'selamat malam',0,'pembuka'),
(45,1256,'Diatmiko',874647857,'saya ingin melihat daftar menu',0,'menu'),
(46,1259,'Diatmiko',874647857,'saya ingin melihat daftar menu makanan',0,'menu'),
(47,1262,'Diatmiko',874647857,'mohon perlihatkan daftar menu',0,'menu'),
(48,1265,'Diatmiko',874647857,'saya ingin melihat daftar menu makanan',0,'menu'),
(49,1268,'Diatmiko',874647857,'saya pesan menu roti bakar 2 kentang goreng 1 dan teh 3',0,'pesan'),
(50,1270,'Diatmiko',874647857,'saya ingin mengulang pesanan',6,'ulang'),
(51,1272,'Diatmiko',874647857,'ya',0,'ulang'),
(52,1274,'Diatmiko',874647857,'saya pesan menu roti bakar 2 kentang goreng 1 dan teh 3',0,'pesan'),
(53,1277,'Diatmiko',874647857,'berapa total pesanan saya',0,'total'),
(54,1280,'Diatmiko',874647857,'saya ingin mengulang pesanan',6,'ulang'),
(55,1282,'Diatmiko',874647857,'ya',0,'ulang'),
(56,1284,'Diatmiko',874647857,'berapa total pesanan saya',0,'total'),
(57,1286,'Diatmiko',874647857,'saya pesan menu roti bakar 2 dan kopi 2',0,'pesan'),
(58,1289,'Diatmiko',874647857,'saya sudah selesai memesan',7,'selesai'),
(59,1293,'Diatmiko',874647857,'ya',0,'selesai'),
(60,1295,'Diatmiko',874647857,'saya ingin melihat daftar menu',0,'menu'),
(61,1298,'Diatmiko',874647857,'saya ingin melihat daftar menu',0,'menu'),
(62,1301,'Diatmiko',874647857,'saya ingin melihat daftar menu',0,'menu'),
(63,1304,'Diatmiko',874647857,'saya ingin melihat daftar menu makanan',0,'menu'),
(64,1307,'nyomanwiartini',1435910777,'/start',0,'mulai'),
(65,1310,'putugedearya',1232554796,'/start',0,'mulai'),
(66,1312,'Diatmiko',874647857,'halo',0,'pembuka'),
(67,1314,'nyomanwiartini',1435910777,'hai',0,'pembuka'),
(68,1316,'putugedearya',1232554796,'selamat malam',0,'pembuka'),
(69,1318,'nyomanwiartini',1435910777,'selamat siang',0,'pembuka'),
(70,1319,'Diatmiko',874647857,'selamat pagi',0,'pembuka'),
(71,1320,'putugedearya',1232554796,'selamat sore',0,'pembuka'),
(72,1324,'nyomanwiartini',1435910777,'saya ingin melihat daftar menu makanan',0,'menu'),
(73,1325,'Diatmiko',874647857,'saya ingin melihat daftar menu',0,'menu'),
(74,1326,'putugedearya',1232554796,'saya ingin melihat daftar menu minuman',0,'menu'),
(75,1333,'nyomanwiartini',1435910777,'saya pesan teh 2',0,'ulang'),
(76,1334,'Diatmiko',874647857,'saya pesan menu roti bakar 2',0,'pesan'),
(77,1335,'putugedearya',1232554796,'saya pesan kentang goreng 3',0,'pesan'),
(78,1341,'nyomanwiartini',1435910777,'saya pesan menu teh 2',0,'pesan'),
(79,1344,'Diatmiko',874647857,'saya ingin mengulang pesanan',6,'ulang'),
(80,1346,'putugedearya',1232554796,'saya sudah selesai memesan',7,'selesai'),
(81,1348,'nyomanwiartini',1435910777,'berapa total pesanan saya',0,'total'),
(82,1351,'Diatmiko',874647857,'y',0,'ulang'),
(83,1352,'putugedearya',1232554796,'y',0,'selesai'),
(84,1357,'Diatmiko',874647857,'saya ingin memesan menu roti bakar 4',0,'pesan'),
(85,1360,'nyomanwiartini',1435910777,'saya sudah selesai memesan',7,'selesai'),
(86,1363,'Diatmiko',874647857,'saya sudah selesai memesan',7,'selesai'),
(87,1368,'nyomanwiartini',1435910777,'y',0,'selesai'),
(88,1369,'Diatmiko',874647857,'y',0,'selesai'),
(89,1372,'putugedearya',1232554796,'saya pesan menu kopi 5',0,'pesan'),
(90,1373,'nyomanwiartini',1435910777,'saya pesan menu kentang goreng 3',0,'pesan'),
(91,1374,'Diatmiko',874647857,'saya memesan menu roti bakar 4',0,'pesan'),
(92,1381,'Diatmiko',874647857,'saya sudah selesai memesan',7,'selesai'),
(93,1382,'nyomanwiartini',1435910777,'saya sudah selesai memesan',7,'selesai'),
(94,1383,'putugedearya',1232554796,'saya sudah selesai memesan',7,'selesai'),
(95,1393,'Diatmiko',874647857,'y',0,'selesai'),
(96,1394,'nyomanwiartini',1435910777,'y',0,'selesai'),
(97,1395,'putugedearya',1232554796,'y',0,'selesai'),
(98,1399,'Diatmiko',874647857,'ssya inhin melhat daftr mrnu',0,'menu'),
(99,1402,'Diatmiko',874647857,'wadaw wadaw gak tuh',0,'bingung');

/*Table structure for table `tb_menu` */

DROP TABLE IF EXISTS `tb_menu`;

CREATE TABLE `tb_menu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jenis` varchar(50) DEFAULT NULL,
  `nama` varchar(50) DEFAULT NULL,
  `harga` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_menu` */

insert  into `tb_menu`(`id`,`jenis`,`nama`,`harga`) values 
(1,'makanan','Roti Bakar',7000),
(2,'makanan','Kentang Goreng',5000),
(3,'minuman','Kopi',4000),
(4,'minuman','Teh',2000);

/*Table structure for table `tb_pencocokan` */

DROP TABLE IF EXISTS `tb_pencocokan`;

CREATE TABLE `tb_pencocokan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jenis` varchar(50) DEFAULT NULL,
  `isi` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_pencocokan` */

insert  into `tb_pencocokan`(`id`,`jenis`,`isi`) values 
(1,'pembuka','hai'),
(2,'pembuka','halo'),
(3,'pembuka','selamat'),
(4,'pembuka','pagi'),
(5,'pembuka','siang'),
(6,'pembuka','sore'),
(7,'pembuka','malam'),
(8,'menu','lihat'),
(9,'menu','daftar'),
(10,'menu','menu'),
(11,'menu','makan'),
(12,'menu','minum'),
(13,'pesan','pesan'),
(16,'pesan','menu'),
(17,'total','berapa'),
(18,'total','total'),
(19,'total','pesan'),
(20,'ulang','pesan'),
(21,'selesai','selesai'),
(22,'selesai','pesan'),
(23,'ulang','ulang'),
(24,'pesan','mes'),
(25,'pesan','roti'),
(26,'pesan','bakar'),
(27,'pesan','kentang'),
(28,'pesan','goreng'),
(29,'pesan','teh'),
(30,'pesan','kopi');

/*Table structure for table `tb_pesanan` */

DROP TABLE IF EXISTS `tb_pesanan`;

CREATE TABLE `tb_pesanan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_order` varchar(30) DEFAULT NULL,
  `tanggal_waktu` datetime DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `chat_id` int(11) DEFAULT NULL,
  `total_harga` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_pesanan` */

insert  into `tb_pesanan`(`id`,`id_order`,`tanggal_waktu`,`username`,`chat_id`,`total_harga`) values 
(1,'1608515006Diatmiko','2020-12-21 09:43:26','Diatmiko',874647857,18000),
(2,'1608529558Diatmiko','2020-12-21 13:45:58','Diatmiko',874647857,18000),
(3,'1608733931Diatmiko','2020-12-23 22:32:11','Diatmiko',874647857,22000),
(4,'1608816417putugedearya','2020-12-24 21:26:57','putugedearya',1232554796,15000),
(5,'1608816494nyomanwiartini','2020-12-24 21:28:14','nyomanwiartini',1435910777,4000),
(6,'1608816498Diatmiko','2020-12-24 21:28:18','Diatmiko',874647857,28000),
(7,'1608816674Diatmiko','2020-12-24 21:31:14','Diatmiko',874647857,28000),
(8,'1608816677nyomanwiartini','2020-12-24 21:31:17','nyomanwiartini',1435910777,15000),
(9,'1608816679putugedearya','2020-12-24 21:31:19','putugedearya',1232554796,20000);

/*Table structure for table `tb_respon` */

DROP TABLE IF EXISTS `tb_respon`;

CREATE TABLE `tb_respon` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `jenis` varchar(50) DEFAULT NULL,
  `jenis_tbh` varchar(50) DEFAULT NULL,
  `respon` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tb_respon` */

insert  into `tb_respon`(`id`,`jenis`,`jenis_tbh`,`respon`) values 
(1,'pembuka','hai','Hai! Ada yang bisa saya bantu?'),
(2,'pembuka','halo','Halo! Ada yang bisa saya bantu?'),
(3,'pembuka','pagi','Selamat pagi! Ada yang bisa saya bantu?'),
(4,'pembuka','siang','Selamat siang! Ada yang bisa saya bantu?'),
(5,'pembuka','sore','Selamat sore! Ada yang bisa saya bantu?'),
(6,'pembuka','malam','Selamat malam! Ada yang bisa saya bantu?'),
(7,'menu',NULL,'Berikut daftar menunya.'),
(8,'pesan','anda','Anda ingin memesan apa?'),
(9,'total',NULL,'Berikut total pesanan anda.'),
(10,'ulang','pesan','Pesanan anda telah kami ulang.'),
(11,'selesai','pesan','Pesanan anda sudah kami terima.'),
(12,'pembuka','awal','Selamat datang di restoran kami! Perkenalkan saya adalah bot pelayan. Ada yang bisa saya bantu?'),
(13,'bingung',NULL,'Maaf saya tidak mengerti. Mohon ulangi kembali.'),
(15,'pesan','telah','Anda telah membuat pesanan. Harap mengulang pesanan apabila terdapat perubahan.'),
(16,'pesan','salah','Terdapat kesalahan dalam memasukan pesanan. Harap dicoba kembali.'),
(17,'pesan','langsung','Harap memasukkan menu yang akan dipesan secara langsung.'),
(18,'pesan','terima','Pesanan diterima. Berikut pesanan anda.'),
(19,'ulang','berhasil','Pesanan berhasil diulang. Harap membuat pesanan kembali.'),
(20,'ulang','tidak','Pesanan tidak jadi diulang.'),
(21,'ulang','apa','Apakah anda yakin ingin mengulang pesanan? (ya/tidak)'),
(22,'belum',NULL,'Anda belum membuat pesanan. Harap membuat pesanan terlebih dahulu.'),
(23,'selesai','tidak','Pesanan tidak jadi dicatat ke sistem.'),
(24,'selesai','apa','Apakah anda yakin sudah selesai membuat pesanan? (ya/tidak)'),
(25,'selesai','berikut','Berikut adalah pesanan yang telah anda buat.');

/*Table structure for table `tmp_pesanan` */

DROP TABLE IF EXISTS `tmp_pesanan`;

CREATE TABLE `tmp_pesanan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `chat_id` int(11) DEFAULT NULL,
  `id_menu` int(11) DEFAULT NULL,
  `nama_menu` varchar(50) DEFAULT NULL,
  `nama_simpel` varchar(50) DEFAULT NULL,
  `kuantitas` int(11) DEFAULT NULL,
  `harga_menu` int(11) DEFAULT NULL,
  `total_menu` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4;

/*Data for the table `tmp_pesanan` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
