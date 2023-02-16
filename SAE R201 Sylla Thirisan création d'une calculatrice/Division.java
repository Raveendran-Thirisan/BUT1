public class Division extends Operation{

  public Division(Expression Operande1,Expression Operande2){
    super(Operande1,Operande2);
  }

  public int valeur()throws ArithmeticException {
    return this.getOperande1().valeur() / this.getOperande2().valeur();

  }

  public String toString(){
    return "(" + getOperande1() + ")" + "/" + "(" + getOperande2()+ ")";

  }

}
