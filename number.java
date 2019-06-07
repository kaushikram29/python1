import java.util.*;
import java.lang.*;
import java.io.*;
public class Rep_num
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		int A[]=new int[N];
		for(int i=0;i<N;i++)
		{
			A[i]=sc.nextInt();
		}
		int B=0;
		for(int i=0;i<N;i++)
		{
			int COUNT=0;
			if(A[i]!=-1)
			{
				for(int j=i;j<N;j++)
				{
					if(A[i]==A[j]&&i!=j)
					{
						A[j]=-1;
						count++;
					}
				}
			}
			if(count==0)
			{
				A[i]=-1;
				B++;
			}
		}
		int T;
		for(int i=0;i<N;i++)
		{
			for(int j=i;j<N;j++)
			{
				if(A[i]>A[j])
				{
					T=A[i];
					A[i]=A[j];
					A[j]=T;
				}
			}
			if(A[i]!=-1)
			{
				System.out.print(A[i]+" ");
			}
		}
		if(B==N)
		{
			System.out.print("unique");
		}
	}
}
