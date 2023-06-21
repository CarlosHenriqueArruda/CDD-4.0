package fundamentos;

import java.util.Scanner;

public class Exercicio11 {

	public static void main(String[] args) {

		System.out.println("Digite o primeiro numero:");
		Scanner dados = new Scanner(System.in);
		double n1 = dados.nextDouble();
		
		System.out.println("Digite o segundo numero:");
		double n2 = dados.nextDouble();
		
		System.out.println("Digite o terceiro numero:");
		double n3 = dados.nextDouble();
		
		System.out.println(n1 > n2 && n1 > n3 ? "O primeiro numero é o maior":
			n2 > n1 && n2 > n3 ? "O segundo numero é o maior":
			n3 > n1 && n3 > n2 ? "O terceiro numero é o maior":
			n1 < n2 && n1 < n3 ? "O primeiro numero é o menor":
			n2 < n1 && n2 < n3 ? "O segundo numero é o menor":
			"O terceiro numero é o menor");

	}

}
