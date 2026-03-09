import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o código de status (1=Disponínel, 2=Reposição, 3=Descontinuado): ");
        int codigo_status = scanner.nextInt();

        switch (codigo_status) {
            case 1:
                System.out.println("Status: Disponível.");
                break;
            case 2:
                System.out.println("Status: Em Reposição.");
                break;
            case 3:
                System.out.println("Status: Descontinuado.");
                break;
            default:
                System.out.println("Código de status inválido.");
        }
        
        scanner.close();
    }
    
}