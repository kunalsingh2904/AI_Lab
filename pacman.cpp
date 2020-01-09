#include <iostream>
#include <string.h>
#include <vector>
#include <fstream>
#include <queue>
#include <stack>
using namespace std;


int nv=0;
int plen=0;



struct cell{
  int x;
  int y;
};

struct adj{
  vector <cell> list;
};



struct graph{
  int level = 0;
  cell parent;
  int color=0;
};



void traceprint(vector<string> str, vector <vector<graph>>  &g, cell goal,cell root)
{
  cell tc;
  tc = goal;
  while(g[tc.x][tc.y].parent.x != root.x || g[tc.x][tc.y].parent.y != root.y )
  {
    str[tc.x][tc.y] = '0';

    tc = g[tc.x][tc.y].parent;   plen++;
  }   
  str[tc.x][tc.y] = '0';
  str[0][0]  = '0';  
  str[root.x][root.y]  = '0'; plen = plen + 3;
  
  
  
  

cout<<nv<<"\n"<<plen<<"\n";

for(int i=0;i<=str.size()-1;i++ )
{
  cout<<str[i]<<"\n";
}

}








void movegen(stack <cell> &st, cell root, vector <vector<adj>> &adjan, vector <vector<graph>>  &g )
{

for(unsigned int k=0;k<=adjan[root.x][root.y].list.size()-1;k++  )
   {
    if(g[adjan[root.x][root.y].list[k].x][adjan[root.x][root.y].list[k].y].color == 0)
    {
      st.push(adjan[root.x][root.y].list[k]  );
      g[adjan[root.x][root.y].list[k].x][adjan[root.x][root.y].list[k].y].color = 1;
          nv++;
      g[adjan[root.x][root.y].list[k].x][adjan[root.x][root.y].list[k].y].parent = root;
      g[adjan[root.x][root.y].list[k].x][adjan[root.x][root.y].list[k].y].level = g[ g[adjan[root.x][root.y].list[k].x][adjan[root.x][root.y].list[k].y].parent.x  ][g[adjan[root.x][root.y].list[k].x][adjan[root.x][root.y].list[k].y].parent.y].level + 1;


    }
   }

}

int  goaltest(cell obs,cell goal)
{
  if( obs.x == goal.x && obs.y == goal.y )
  {
    return 1;
  }
  else
  {
    return -1;
  }
}
//hidden DFS_s 
  void DFS_s(vector <vector<adj>> &adjan, vector <vector<graph>>  &g, cell root, cell goal)
  {

  stack <cell> st;
  
  movegen(st,root,adjan,g);
  
  g[root.x][root.y].color = 1;  nv++;
  g[root.x][root.y].parent = root;


  while( !st.empty() )
  {
    if(goaltest(st.top(),goal) == 1)
    {
      
      break;  

    }
    else
    {
      // cout<<"That "<<st.top().x<<" "<<st.top().y<<"\n";

      cell tc = st.top();
      st.pop();
      //g[tc.x][tc.y].color = 1;
      movegen( st ,tc, adjan,g);

    }
    
  }

  }





//DFID
  int DFS_dep(vector <vector<adj>> &adjan, vector <vector<graph>>  g, cell root, cell goal, int dep,vector<string> str)
  {

  stack <cell> st;
  st.push(root);

  if( dep > 0)
    {
      movegen(st,root,adjan,g);

    }

  g[root.x][root.y].color = 1;  nv++;
  g[root.x][root.y].parent = root;

  

  while( !st.empty() )
  {
    if(goaltest(st.top(),goal) == 1 )
    {
      
      traceprint(str, g, goal, root);

      return 1;  

    }
    else
    {

      cell tc = st.top();
      st.pop();

      if( g[tc.x][tc.y].level < dep )
      {
        movegen( st ,tc, adjan,g);
        
      }

    }
    
  }
  return -1;

  }

  void DFid(vector <vector<adj>> &adjan, vector <vector<graph>>  &g, cell root, cell goal, vector<string> str  )
  {
    int depth = 0;
    while(  DFS_dep(adjan, g, root, goal, depth, str) != 1 )
    {
      
      depth++;
    }

  }





void dispadj(vector <vector<adj>> &adjan, int n, int m)
{
//hidden display adj
  for(int i=0;i<=n-1;i++ ) // display adj
  {
    for(int j=0;j<=m-1;j++ )

      {
        cout<<i<<" "<<j<<" : ";
        if(adjan[i][j].list.size() != 0)
        {
          for(unsigned int k=0;k<=adjan[i][j].list.size()-1;k++  )
          {
            cout<<"|"<<adjan[i][j].list[k].x<<" "<<adjan[i][j].list[k].y<<"| ";
          }
        }
        cout<<"\n";
      }
  }
}










int main(int argc,char** argv)
{

vector<string> str;
string tstr;
int i=0;
ifstream infile(argv[1]);



int typ;
infile>>typ;

infile.ignore();




while(getline(infile,tstr,'\n') ){

  str.push_back(tstr);
  i++;
}
// for(int i=0;i<=str.size()-1;i++ )    // disp grid
// {
//   cout<<str[i]<<"\n";
// }

int n =str.size();
int m = strlen(str[0].c_str());
//cout<<"nxm "<<n<<" "<<m<<"\n";

vector <vector<adj>> adjan(n,vector<adj>(m));

//hidden code
  cell root; cell goal;
  cell cc;


  for(int i=1;i<=n-1;i++ )
  {
  if(str[i][0]==' ')
    {
      cell cc;
      cc.x = i; cc.y = 1;
      adjan[i][0].list.push_back(cc);
      root.x = i; root.y = 0;
    }

  if(str[i][0]=='*')
      {
      goal.x = i; goal.y = 0;     
      }

  }

  for(int i=1;i<=n-1;i++ )
  {
    if(str[i][m-1]==' ')
      {
        cell cc;
        cc.x = i; cc.y = m-2;
        adjan[i][m-1].list.push_back(cc);
        root.x = i; root.y = m-2;
      }
      if(str[i][m-1]=='*')
          {

          goal.x = i; goal.y = m-1;     
          }

  }
  for(int j=1;j<=m-1;j++ )
  {
    if(str[0][j]==' ')
      {
        cell cc;
        cc.x = 1; cc.y = j;
        adjan[0][j].list.push_back(cc);
        root.x = 0; root.y = j;
      }
      if(str[0][j]=='*')
          {

          goal.x = 0; goal.y = j;     
          }
  }
  for(int j=1;j<=m-1;j++ )
  {
    if(str[n-1][j]==' ')
      {
        cell cc;
        cc.x = n-2; cc.y = j;
        adjan[n-1][j].list.push_back(cc);
        root.x = n-1; root.y = j;
      }
      if(str[n-1][j]=='*')
          {

          goal.x = n-1; goal.y = j;     
          }

  }




//hidden code;adj,goal etc;
  for(int i=1;i<=n-1-1;i++ )
  {
    for(int j=1;j<=m-1-1;j++ )

      {
        if(str[i][j] == ' ')
        {

               if(  str[i+1][j] ==' ' ) // UP
               {

                cell ct;
                ct.x = i+1;
                ct.y = j;

                adjan[i][j].list.push_back(ct);


              }


               if(  str[i-1][j] ==' ' ) // DOWN
               {

                cell ct;
                ct.x = i-1;
                ct.y = j;

                adjan[i][j].list.push_back(ct);


              }



              if(  str[i][j+1] ==' ' ) // RIGHT
              {

                cell ct;
                ct.x = i;
                ct.y = j+1;

                adjan[i][j].list.push_back(ct);


              }

              if(  str[i][j-1] ==' ' ) // LEFT
              {

                cell ct;
                ct.x = i;
                ct.y = j-1;

                adjan[i][j].list.push_back(ct);


              }



             




          }

      }

  }
  {//goal 
    if(str[goal.x][goal.y-1] == ' ')
    {
      cell ct;
      ct.x = goal.x;
      ct.y = goal.y;

      adjan[goal.x][goal.y-1].list.push_back(ct);

    }
        if(str[goal.x-1][goal.y] == ' ')
    {
      cell ct;
      ct.x = goal.x;
      ct.y = goal.y;

      adjan[goal.x-1][goal.y].list.push_back(ct);

    }
        if(str[goal.x][goal.y+1] == ' ')
    {
      cell ct;
      ct.x = goal.x;
      ct.y = goal.y;

      adjan[goal.x][goal.y+1].list.push_back(ct);

    }
        if(str[goal.x+1][goal.y] == ' ')
    {
      cell ct;
      ct.x = goal.x;
      ct.y = goal.y;

      adjan[goal.x+1][goal.y].list.push_back(ct);

    }

  }


vector <vector<graph>> g(n,vector<graph>(m)); // graph fixed index


dispadj(adjan,n,m);





//cout<<"root "<<root.x<<" "<<root.y<<"\n";
//cout<<"goal "<<goal.x<<" "<<goal.y<<"\n";


if(typ == 1)
{
  DFS_s(adjan,g,root,goal);
  traceprint(str, g, goal, root);

}
else if(typ == 2)
{
  DFid(adjan, g, root, goal, str);
}
else
{
cout<<typ<<" search type not clear";
}






  return 0;
}
