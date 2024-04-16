
```mermaid
 classDiagram
      SudokuApp "1" --> "1" SudokuMatrix
      class SudokuApp{
          + SudokuMatrix sudoku
          + String level
          start()
      }
      class SudokuMatrix{
          + String level
          + List matrix
          insert_number()
      }
      SudokuMatrix "1" --> "1" FileService
      class FileService{
          + String easy
          + String medium
          + String hard
          + String path
          create_matrix()
      }
```