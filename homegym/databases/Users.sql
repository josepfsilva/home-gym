CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    Username TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    BirthDate DATE NOT NULL,
    RegistrationDate DATE NOT NULL,
    Role ENUM('Admin', 'User', 'UserHelper') NOT NULL DEFAULT 'User',
    Status ENUM('Online', 'Offline') NOT NULL DEFAULT 'Online'
    MeasurementsID INT UNIQUE,
    FOREIGN KEY (MeasurementsID) REFERENCES Measurements(MeasurementsID)
);

