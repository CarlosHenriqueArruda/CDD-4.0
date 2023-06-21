package fundamentos;
import java.util.Scanner;
//Primeiro exercicio em java usando tenario
public class Exercicio10 {

	public static void main(String[] args) {
		Scanner dados = new Scanner(System.in);
		System.out.println("Digite um numero:");
		double resp = dados.nextDouble();
		System.out.println(resp == 0 ? "Neutro":resp > 0 ? "Positivo":"Negativo");
	}

}
