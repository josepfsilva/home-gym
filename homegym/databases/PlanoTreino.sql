CREATE TABLE PlanoTreino (
    PlanoID INT PRIMARY KEY AUTO_INCREMENT,
    Nome TEXT UNIQUE NOT NULL,
    Descricao TEXT NOT NULL,
    Tipo ENUM('Cardio', 'Musculacao') NOT NULL DEFAULT 'Musculacao',
    PlanoExercicioID INT NOT NULL,
    FOREIGN KEY (PlanoExercicioID) REFERENCES PlanoExercicios(PlanoExercicioID)
);