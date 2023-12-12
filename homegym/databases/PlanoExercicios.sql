CREATE TABLE PlanoExercicios (
    PlanoExercicioID INT PRIMARY KEY AUTO_INCREMENT,
    Exercicio1 INT NOT NULL,
    Exercicio2 INT NOT NULL,
    Exercicio3 INT NOT NULL,
    FOREIGN KEY (Exercicio1) REFERENCES Exercicios(ExercicioID)
    FOREIGN KEY (Exercicio2) REFERENCES Exercicios(ExercicioID)
    FOREIGN KEY (Exercicio3) REFERENCES Exercicios(ExercicioID)

);