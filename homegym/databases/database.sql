CREATE TABLE IF NOT EXISTS BadgeType (
    BadgeID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT UNIQUE NOT NULL,
    Description TEXT NOT NULL,
    Type TEXT NOT NULL, 
    Image BLOB NOT NULL,
    Requirements TEXT NOT NULL
);



CREATE TABLE IF NOT EXISTS ExercisePlan (
    ExercisePlanID INTEGER PRIMARY KEY AUTOINCREMENT,
    Exercise1 INTEGER NOT NULL,
    Exercise2 INTEGER NOT NULL,
    Exercise3 INTEGER NOT NULL,
    FOREIGN KEY (Exercise1) REFERENCES Exercises(ExerciseID),
    FOREIGN KEY (Exercise2) REFERENCES Exercises(ExerciseID),
    FOREIGN KEY (Exercise3) REFERENCES Exercises(ExerciseID)
);


CREATE TABLE IF NOT EXISTS Exercises (
    ExerciseID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Description TEXT NOT NULL,
    URL TEXT NOT NULL,
    ExerciseImg TEXT NOT NULL,
    Type TEXT CHECK( Type IN ('Cardio', 'Musculacao','Meditacao','Alongamento')) NOT NULL DEFAULT 'Musculacao',
    Difficulty TEXT CHECK( Difficulty IN ('Easy', 'Medium', 'Hard')) NOT NULL DEFAULT 'Easy'
);

CREATE TABLE IF NOT EXISTS FinishTraining (
    FinishTrainingID INTEGER PRIMARY KEY AUTOINCREMENT,
    FinishTime Timestamp,
    TrainingDuration TIME,
    Rating INTEGER,
    TrainingPlanID INTEGER NOT NULL,
    FOREIGN KEY (TrainingPlanID) REFERENCES TrainingPlan (TrainingPlanID)
    
);



CREATE TABLE IF NOT EXISTS Food(
    FoodID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT UNIQUE NOT NULL,
    Calories INTEGER NOT NULL
);



CREATE TABLE IF NOT EXISTS Friendship (
    FriendshipID INTEGER PRIMARY KEY AUTOINCREMENT,
    UserID INTEGER NOT NULL,
    FriendID INTEGER NOT NULL,
    Status TEXT CHECK( Status IN('Pending', 'Accepted', 'Declined')) NOT NULL DEFAULT 'Pending',
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (FriendID) REFERENCES User(UserID)
);

CREATE TABLE IF NOT EXISTS Measurements (
    MeasurementsID INTEGER PRIMARY KEY AUTOINCREMENT,
    Height DECIMAL(5,2),
    Weight DECIMAL(5,2),
    BodyFat DECIMAL(4,2),
    Date DATE
);


CREATE TABLE IF NOT EXISTS Nutrition (
    NutritionID INTEGER PRIMARY KEY AUTOINCREMENT,
    FoodID INTEGER NOT NULL,
    Description TEXT UNIQUE NOT NULL,
    FOREIGN KEY (FoodID) REFERENCES Food(FoodID)
    );



CREATE TABLE IF NOT EXISTS TrainingPlan (
    TrainingPlanID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Description TEXT NOT NULL,
    Type TEXT CHECK( Type IN('Cardio', 'Musculacao', 'Meditacao', 'Alongamentos')) NOT NULL DEFAULT 'Musculacao',
    Difficulty TEXT CHECK( Difficulty IN('Easy', 'Medium', 'Hard')) NOT NULL DEFAULT 'Easy',
    PlanDuration INTEGER NOT NULL,
    TrainImage TEXT NOT NULL,
    ExercisePlanID INTEGER NOT NULL,
    UserID INTEGER NOT NULL,
    FOREIGN KEY (ExercisePlanID) REFERENCES ExercisePlan(ExercisePlanID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);



CREATE TABLE IF NOT EXISTS UserBadges (
    UserBadgesID INTEGER PRIMARY KEY AUTOINCREMENT,
    DateAwarded DATETIME NOT NULL,
    BadgeID INTEGER NOT NULL,
    TrainingPlanID INTEGER NOT NULL,
    FOREIGN KEY (TrainingPlanID) REFERENCES TrainingPlan(TrainingPlanID),
    FOREIGN KEY (BadgeID) REFERENCES BadgeType(BadgeID)
);




CREATE TABLE IF NOT EXISTS Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Username TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL,
    Name TEXT NOT NULL,
    Surname TEXT NOT NULL,
    Weight INTEGER NOT NULL,
    Height INTEGER NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    BirthDate DATE NOT NULL,
    RegistrationDate DATE NOT NULL,
    Role TEXT CHECK( Role IN ('Admin', 'User', 'UserHelper')) NOT NULL DEFAULT 'User',
    Status TEXT CHECK( Status IN ('Online', 'Offline')) NOT NULL DEFAULT 'Online',
    MeasurementsID INTEGER UNIQUE,
    FriendshipID INTEGER UNIQUE,
    BadgeID INTEGER UNIQUE,
    FOREIGN KEY (BadgeID) REFERENCES UserBadgesID(BadgeID),
    FOREIGN KEY (MeasurementsID) REFERENCES Measurements(MeasurementsID),
    FOREIGN KEY (FriendshipID) REFERENCES Friendship(FriendshipID)
);




