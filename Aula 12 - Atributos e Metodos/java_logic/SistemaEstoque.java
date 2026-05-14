public class SistemaEstoque {

    public static void main(String[] args) {
        // Criando instâncias distintas no Heap
        Produto poteChocolate = new Produto("Pote Chocolate 2L", 15, 100);
        Produto picoleLimao = new Produto("Picolé de Limão", 50, 100);

        // Testando a inteligência automatizada
        System.out.println("Chocolate precisa repor? " + poteChocolate.verificarNecessidadeCompra()); // True
        System.out.println("Limão precisa repor? " + picoleLimao.verificarNecessidadeCompra());       // False

        // Testando a blindagem contra erros humanos
        poteChocolate.registrarSaida(20);
        // Saída esperada: Mensagem de erro e bloqueio da operação.
    }
}