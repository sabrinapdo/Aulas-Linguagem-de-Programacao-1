import java.util.Scanner;

public class Desafio {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        while (true) {

            System.out.print("Digite o nome do produto: ");
            String nome_do_produto = scanner.nextLine();

            System.out.print("Digite a quantidade em estoque: ");
            int quantidade_em_estoque = scanner.nextInt();

            System.out.print("Digite o preço do produto: ");
            double preco_unitario = scanner.nextDouble();

            if (quantidade_em_estoque >= 0) {
                System.out.println("Nome do produto: " + nome_do_produto +
                        ", quantidade em estoque: " + quantidade_em_estoque +
                        ", preço unitário: " + preco_unitario);
            } else {
                System.out.println("ERRO: a quantidade não pode ser um valor negativo. Por favor, tente novamente.");
            }

            System.out.println();
        }
    }
}