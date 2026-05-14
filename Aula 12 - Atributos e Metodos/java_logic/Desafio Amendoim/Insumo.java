public class Insumo {

    private String nome;
    private int quantidade;
    private int mesValidade;

    public Insumo(String nome, int quantidade, int mesValidade) {

        this.nome = nome;
        this.quantidade = quantidade;

        // Garantindo validade correta
        if (mesValidade >= 1 && mesValidade <= 12) {
            this.mesValidade = mesValidade;
        } else {
            System.out.println("ALERTA: Mês inválido! Definindo validade padrão.");
            this.mesValidade = 1;
        }
    }

    public void setMesValidade(int mes) {

        if (mes >= 1 && mes <= 12) {
            this.mesValidade = mes;
            System.out.println("Mês de validade atualizado com sucesso.");
        } else {
            System.out.println("ALERTA: Valor inválido! Operação bloqueada.");
        }
    }

    public boolean estaValido(int mesAtual) {

        if (this.mesValidade < mesAtual) {
            System.out.println("ALERTA: Risco de Amendoim Murcho! Produto Vencido");
            return false;
        }

        return true;
    }

    public void mostrarDados() {

        System.out.println("\n--- DADOS DO INSUMO ---");
        System.out.println("Nome: " + nome);
        System.out.println("Quantidade: " + quantidade);
        System.out.println("Mês de validade: " + mesValidade);
    }
}