import java.util.Scanner; // Importa a classe para leitura de dados [cite: 11]
import java.util.Locale; // Importa para garantir o uso do ponto decimal em vez de vírgula

public class calculadora {
    public static void main(String[] args) {
        // Configura o ponto como separador decimal (padrão americano/programação)
        Locale.setDefault(Locale.US);

        // Passo 1: instanciar o objeto Scanner para ler a entrada do teclado [cite: 11]
        Scanner sc = new Scanner(System.in);

        //Passo 2: entrada de dados e declaração de variáveis [cite: 6]
        System.out.println(x: "--- Calculadora dde Negócios (Java) ---");

        System.out.print(s: "Digite o primeiro número: ");
        double numero1 = sc.nextDouble(); // Java requer definição explícita do tipo [cite: 6]

        System.out.print(s: "Digite o segundo número: ");
        double numero2 = sc.nextDouble();

        //Passo 3: processamento (cálculos aritméticos) [cite: 7]
        double soma = numero1 + numero2;
        double subtracao = numero1 - numero2;
        double multiplicao = numero1 * numero2;
        double divisao = numero1 / numero2;

        //Passo 4: saída de resultados formatados
        System.out.printf(format: "Soma: %.2f%n", soma);
        System.out.printf(format: "Subtracao: %.2f%n", subtracao);
        System.out.printf(format: "Multiplicação: %.2f%n", multiplicao);
        System.out.printf(format: "Divisão: %.2f%n", divisao);

        // Passo 5: fechar o Scanner (boa prática de gerenciamento de memória)
        sc.close();
    }
}