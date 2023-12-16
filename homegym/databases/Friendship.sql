CREATE TABLE Friendship (
    FriendshipID INT PRIMARY KEY AUTO_INCREMENT,
    UserID INT NOT NULL,
    FriendID INT NOT NULL,
    'Status' ENUM('Pending', 'Accepted', 'Declined') NOT NULL DEFAULT 'Pending',
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (FriendID) REFERENCES User(UserID)
);