/*
  * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package filecompressor;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.net.URL;
import java.util.ArrayList;
import javax.swing.JFrame;

/**
 *
 * @author Alex
 */
public class FileCompressor {

    public static void main(String[] args) {
        URL location = FileCompressor.class.getProtectionDomain().getCodeSource().getLocation();
       
        File f = new File(location.getPath().replace("FileCompressor.jar", ""));
        String[] list = f.list();
        ArrayList<String> fileNames = new ArrayList<>();
        for(String a:list){
            try{
                if(a.substring(0,5).equals("Match")){
                    fileNames.add(location.getPath().replace("FileCompressor.jar","") + a);
                }
            }
            catch(StringIndexOutOfBoundsException e){
            }  
        }
       try{
             File file = new File("CondensedMatches.txt");
             file.createNewFile();
             BufferedWriter writer = new BufferedWriter(new FileWriter(file));
            for(String b:fileNames){
                if(fileNames.size()<1)
                    break;
                try{
                    BufferedReader in = new BufferedReader(new FileReader(new File(b)));
                    writer.append(in.readLine());
                    writer.newLine();
                    }
            catch(Exception e){
                System.out.println(e);
            }
            }
        writer.flush();
        writer.close();
        
        }
       catch(Exception e){}
    }
    
}
