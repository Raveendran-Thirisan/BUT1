public class Nombre extends Expression{
  private int valeurnombre ;

  public int valeur(){
    return valeurnombre;
  }

  public Nombre(int valeurnombre){
    this.valeurnombre = valeurnombre;
  }
    
  public String toString(){
   return  String.valueOf(valeur());

  }



//getter

public int getvaleurnombre(){
  return this.valeurnombre;
}

//setter
public void setvaleurnombre(int val){
   this.valeurnombre = val;
 }
}
