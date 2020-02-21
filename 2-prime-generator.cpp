#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int test,m,n,i,j,k,a=0;
    cin>>test;

      for (i=1; i<=test ;i++)
      {
          cin>>m>>n;
          for (j=m; j<=n; j++)
          {
              for (k=2; k<=sqrt(j); k++)
              {
                  if (j%k==0)
                  {
                    a=1;
                    break;
                  }
              }
          if (a==0 && j!=1)
          cout<<j<<endl;
          a=0;
          }
          cout<<endl;
      }


    return 0;
}

