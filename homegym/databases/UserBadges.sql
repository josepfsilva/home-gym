CREATE TABLE UserBadges (
    UserBadgesID INT PRIMARY KEY AUTO_INCREMENT,
    DateAwarded DATETIME NOT NULL,
    BadgeID INT NOT NULL,
    PlanoTreinoID INT NOT NULL,
    FOREIGN KEY (PlanoTreinoID) REFERENCES PlanoTreino(PlanoID),
    FOREIGN KEY (BadgeID) REFERENCES BadgeType(BadgeID)

)