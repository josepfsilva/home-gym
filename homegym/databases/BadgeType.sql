CREATE TABLE BadgeType (
    BadgeID INT PRIMARY KEY AUTO_INCREMENT,
    Nome TEXT UNIQUE NOT NULL,
    Descricao TEXT NOT NULL,
);