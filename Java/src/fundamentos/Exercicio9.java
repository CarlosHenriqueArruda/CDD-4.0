package fundamentos;
import java.util.Scanner;
public class Exercicio9 {
//Primeiro codigo em Java, pedindo um numero e verificando se é positivo ou negativo!
	public static void main(String[] args) {
		Scanner Dados = new Scanner(System.in);
		System.out.println("Digite um numero:");
		double resp = Dados.nextDouble();
		if (resp >=0)
			System.out.println("Positivo!");
		else
			System.out.println("Negativo!");
	}

}
