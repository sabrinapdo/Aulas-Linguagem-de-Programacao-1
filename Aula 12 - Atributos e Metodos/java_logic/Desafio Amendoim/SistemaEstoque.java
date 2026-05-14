public class SistemaEstoque {

    public static void main(String[] args) {

        Insumo insumo1 = new Insumo("Amendoim", 50, 8);

        insumo1.mostrarDados();

        insumo1.setMesValidade(10);

        insumo1.setMesValidade(15);

        System.out.println("\nProduto válido? " + insumo1.estaValido(7));

        System.out.println("\nProduto válido? " + insumo1.estaValido(11));
    }
}