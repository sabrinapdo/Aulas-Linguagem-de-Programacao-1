import java.util.Scanner;

public class DesafioRoi {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o ganho: ");
        double ganho = scanner.nextDouble();

        System.out.print("Digite o investimento: ");
        double investimento = scanner.nextDouble();

        if (investimento == 0) {
            System.out.println("Erro: investimento não pode ser zero.");
        } else {
            double roi = ((ganho - investimento) / investimento) * 100;
            System.out.println("ROI: " + roi + "%");
        }

        scanner.close();
    }
}
