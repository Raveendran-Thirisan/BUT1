public class Addition extends Operation{


public Addition(Expression Operande1,Expression Operande2){
  super(Operande1,Operande2);
}

  public int valeur(){
    return this.getOperande1().valeur() + this.getOperande2().valeur();
  }

  public String toString(){
   return "le résultat de l'addition est "+ getOperande1() + "+" + getOperande2();
  }

}





