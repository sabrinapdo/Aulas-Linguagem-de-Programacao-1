import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite a quantidade em estoque: ");
        int quantidade = scanner.nextInt();
    
        if (quantidade < 1) {
            System.out.println("Status: em falta");
        } else if (quantidade < 5) {
            System.out.println("Status: alerta de estoque baixo.");
        } else {
            System.out.println("Status: estoque OK.");
        }
        
        scanner.close();
    }
}
