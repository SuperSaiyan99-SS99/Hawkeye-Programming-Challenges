package stuff;

import java.util.Scanner;

public class Division2_2017_Rock_Paper_Scissors {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String userFirstChoice = input.nextLine();
		String userSecondChoice = input.nextLine();
				
		if (userFirstChoice.equals(userSecondChoice)) {
			System.out.println("Tie");
		}

		if(userFirstChoice.equals("R") && userSecondChoice.equals("S")) {
			System.out.println(userFirstChoice);
		}
		
		if(userFirstChoice.equals("R") && userSecondChoice.equals("P")) {
			System.out.println(userSecondChoice);
		}
		
		
		if(userFirstChoice.equals("S") && userSecondChoice.equals("R")) {
			System.out.println(userSecondChoice);
		}
		
		if(userFirstChoice.equals("S") && userSecondChoice.equals("P")) {
			System.out.println(userFirstChoice);
		}
		
		input.close();
	}	
}
