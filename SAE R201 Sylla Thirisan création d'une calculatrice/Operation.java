public abstract class Operation extends Expression{

private Expression Operande1;
private Expression Operande2;


public Operation (Expression Operande1, Expression Operande2){
  this.Operande1 = Operande1;
  this.Operande2 = Operande2;
}

  public Operation(Operation obj){
    this.Operande1 = obj.Operande1;
    this.Operande2 = obj.Operande2;
  }


//getters


public Expression getOperande1(){
  return this.Operande1;
}
public Expression getOperande2(){
  return this.Operande2;
}

//setters

public void setOperande1(Expression ope){
  this.Operande1 = ope;

}

public void setOperande2(Nombre ope){
  this.Operande2 = ope;

}



}
