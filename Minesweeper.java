/*
Samuel Kim
CECS 277 02/10/2022
LAB 3 - 2D Arrays
*/
import java.util.Scanner;
import java.util.Random;

class Main {  
  static void placeMines(int[][] grid, int mines){
    Random rand = new Random();
    int row1 = 0;
    int col1 = 0;
    for (int num = 0; num < mines; num++){
     /* creating first random values, then if the slot is already a 9, go into the while loop and search again for an empty index */
      row1 = rand.nextInt(grid.length);
      col1 = rand.nextInt(grid[0].length);
      while (grid[row1][col1] == 9){
        row1 = rand.nextInt(grid.length);
        col1 = rand.nextInt(grid[0].length);
        }
      /* at this point the index will never be 9 and not we can assign 9 to the index */
      grid[row1][col1] = 9;
    }
  }
  static void fillGrid(int[][] grid){
    int count = 0;
    for (int num = 0; num < grid.length; num++){
      for (int j = 0; j < grid[0].length; j++){
        if (grid[num][j] != 9){
          /* need 4 + 4 + 1 = 9 if statements to check if the index position is on a boundary: */
          
          /* top left corner: */
          if (num == 0 && j == 0){
            for (int q = 0; q <= 1; q++){
              for ( int w = 0; w <= 1; w++){
                if (grid[q][w] == 9){
                  count += 1;
                    }
                }
            }
            grid[num][j] = count;
            count = 0;
          }
          /* top right corner */
          else if (num == 0 && j == grid[0].length - 1){
            for (int q = 0; q <= 1; q++)          {
              for ( int w = grid[0].length - 1; w >= grid[0].length - 2; w--){
                if (grid[q][w] == 9){
                  count += 1;
                }
                }
              }
            grid[num][j] = count;
            count = 0;
          }
         /* bottom right corner */ 
          else if (num == grid.length - 1 && j == grid[0].length - 1){
            for (int q = grid.length - 1; q >= grid.length - 2; q--)          {
              for ( int w = grid[0].length - 1; w >= grid[0].length - 2; w--){
                if (grid[q][w] == 9){
                  count += 1;
                }
                }
              }
            grid[num][j] = count;
            count = 0;
          }
        /* bottom left corner */
          else if (num == grid.length - 1 && j == 0){
            for (int q = grid.length - 1; q >= grid.length - 2; q--)          {
              for ( int w = 0; w <= 1; w++){
                if (grid[q][w] == 9){
                  count += 1;
                }
                }
              }
            grid[num][j] = count;
            count = 0;
          }
        /* top row */
          else if (num == 0){
            for (int q = 0; q <= 1; q++){
              for ( int w = -1; w <= 1; w++){
                if (grid[q][j + w] == 9){
                  count += 1;
                    }
                }
            }
            grid[num][j] = count;
            count = 0;
          }
        /* bottom row */
          else if (num == grid.length - 1){
            for (int q = grid.length - 1; q >= grid.length - 2; q--){
              for ( int w = -1; w <= 1; w++){
                if (grid[q][j + w] == 9){
                  count += 1;
                    }
                }
            }
            grid[num][j] = count;
            count = 0;
          }
        /* left column */
          else if (j == 0){
            for (int q = -1; q <= 1; q++){
              for ( int w = 0; w <= 1; w++){
                if (grid[num + q][w] == 9){
                  count += 1;
                    }
                }
            }
            grid[num][j] = count;
            count = 0;
          }
        /* right column */
          else if (j == grid[0].length - 1){
            for (int q = -1; q <= 1; q++){
              for ( int w = grid[0].length - 1; w >= grid[0].length - 2; w--){
                if (grid[num + q][w] == 9){
                  count += 1;
                    }
                }
            }
            grid[num][j] = count;
            count = 0;
          }
        /* rest of the indexes */
          else {
            for (int q = -1; q <= 1; q++){
              for ( int w = -1; w <= 1; w++){
                if (grid[num + q][j + w] == 9){
                  count += 1;
                    }
                }
            }
            grid[num][j] = count;
            count = 0;
          }
        }
      }
    }
  }
  static void displayGrid(int[][] grid){
    for (int num = 0; num < grid.length; num++){
      System.out.println("");
      for (int j = 0; j < grid[0].length; j++){
        System.out.print("[" + Integer.toString(grid[num][j]) + "] ");
      }
    }
  }
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    System.out.println("Minesweeper maker!!"); 
    System.out.println("Enter number of Rows (5-10): "); 
    int rows = in.nextInt();
    System.out.println("Enter number of Columns (5-10): "); 
    int columns = in.nextInt();
    System.out.println("Enter number of Mines (5-10): "); 
    int mines = in.nextInt();
    int [][] grid = new int [rows][columns];
    placeMines(grid, mines);
    fillGrid(grid);
    displayGrid(grid);
  } 
}

