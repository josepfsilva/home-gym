CREATE TABLE Exercicios (
    ExercicioID INT PRIMARY KEY AUTO_INCREMENT,
    Nome TEXT UNIQUE NOT NULL,
    Descricao TEXT NOT NULL,
    URL TEXT NOT NULL,
    Tipo ENUM('Cardio', 'Musculacao') NOT NULL DEFAULT 'Musculacao',
    Difficulty ENUM('Easy', 'Medium', 'Hard') NOT NULL DEFAULT 'Easy'
);