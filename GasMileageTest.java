import java.util.Scanner;

public class GasMileageTest
{
   public static void main(String[]args)
   {
      Scanner input = new Scanner(System.in);
      
      double mpg =0 ; 
      int totalm =0 ; //total gallons 
      int totalg =0; //total miles
      int tripcount=0; 
      
      // Enter miles with scanner//
      
      System.out.print("Enter miles or -1 to quit:");
      int miles = input.nextInt();
      
      while(miles != -1 )
      {
      totalm = totalm + miles; 
      
      System.out.print("Enter gallons or -1 to quit :");
      int gallons = input.nextInt();
      
      totalg = totalg + gallons;
      tripcount = tripcount + 1;
      
      mpg  = (double)miles/gallons;
      System.out.printf("Miles per gallon on Trip %.2f%n",mpg);
      
      }
      if(tripcount !=0)
      {
      
      double totalavg  = (double)mpg/tripcount; 
      System.out.printf("Miles per gallon on Trip %.2f%n",totalavg); 
      
      
      }

      else
      
      System.out.printf("Nothing was entered"); 

      }
  
   }
   
   
   

   
   