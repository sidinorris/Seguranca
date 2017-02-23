import java.util.*;
import java.io.*;
import java.nio.file.*;

class padroes{
    public static void main(String [] args)throws IOException{
        byte[] input = Files.readAllBytes(Paths.get("entrada.txt"));
        ArrayList <String> lidos = new ArrayList <String>();
        for(int cont= 0; cont < input.length; cont++){
            boolean achou = false;
            for(int contx= 0; contx < lidos.size(); contx++)
                if(lidos.get(contx).equals("" + (char)input[cont]) || (char)input[cont] == '\n')
                    achou = true;
                if(!achou)
                  lidos.add("" + (char)input[cont]);
        }
        System.out.print("Entrada: " + new String(input, "UTF-8"));
        for(int cont = 0; cont < input.length; cont++)
            for(int contx = 0; contx < lidos.size(); contx++)
                if(lidos.get(contx).equals("" + (char)input[cont]))
                    System.out.println(lidos.get(contx) + ": " + contx);
    }
}
