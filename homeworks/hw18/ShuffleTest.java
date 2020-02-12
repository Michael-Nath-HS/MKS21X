/*
3. Empirical Shuffle check.
   Run computational experiments to check that our shuffling code works
   as advertised. Write a program ShuffleTest that takes two integer
   command-line arguments m and n, does n shuffles on an array of length
   m that is initialized with a[i] = i before each shuffle, and prints
   an m-by-m table such that row i gives the number of times i wound up
   in position j for all j. All values in the resulting array should
   be close to n / m.

    Shuffle Code:
      int n = deck.length; 
      for (int i = 0; i < n; i++) { 
      	  int r = i + (int) (Math.random() * (n-i)); 
   	  String temp = deck[r];
   	  deck[r] = deck[i];
   	  deck[i] = temp;
      } 
*/
public class ShuffleTest{

    public static void main(String [] args){
	int m = Integer.parseInt(args[0]); // m cards
	int n = Integer.parseInt(args[1]); // n trials
	int [] perm = new int[m];
	int[][] results = new int[m][m];

	for (int trial  = 0; trial < n; trial++){
	    // initialize perm: 0,1,2, ..., m - 1
	    for (int i = 0; i < m; i++)
		perm[i] = i;
	    
	    // shuffle perm[] 
	    for (int i = 0; i < m; i++) { 
		int r = i + (int) (Math.random() * (m-i)); 
		int temp = perm[r];
		perm[r] = perm[i];
		perm[i] = temp;
	    }
	    // ************************************************************
	    // record results
	    // YOUR CODE GOES HERE
      	    // ************************************************************
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < m; j++) {
				if (i == perm[j]) {
					results[i][j]++;
				}
			}
		}
	}	    
	// print the results table
	for (int i = 0; i < m; i++){
	    for(int j = 0; j < m; j++){
		System.out.print(1.0 * results[i][j] / n + " ");
	    }
	    System.out.println();
	}

    }

}
