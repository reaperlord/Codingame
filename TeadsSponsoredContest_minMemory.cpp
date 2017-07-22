#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
 
class node
{
      public:
      
      
      
      node(int inputIdentity) : 
           noOfLinks(0) //, maxGenAnceEvalFlag(0)
      {
              identity=inputIdentity;
      }
      
      
      int getIdentity()
      {
          return identity;
      }
      
      void addLink(node* linkToAdd)
      {
          links.push_back(linkToAdd);
          traversedFromEvalFlag.push_back(false);
          traversedFromVal.push_back(0);
          ++noOfLinks;
      }
       
      int findMaxTraversalValue( node* ptrOfOriginNode) 
      {
          if ((ptrOfOriginNode!=this)&&( noOfLinks==1))
          {
              traversedFromEvalFlag[0]=true;
              traversedFromVal[0]=0;
              return traversedFromVal[0];
          }
          
          int i;
          for (i=0; i<links.size(); ++i)
          {
              if (links[i]==ptrOfOriginNode)
              {
                if (traversedFromEvalFlag[i])
                    return traversedFromVal[i];
                else
                    break;
              }
          }
          
          int minTraversal=0;
          
          for (int j=0; j<links.size(); ++j)
          {
              if (j==i)
                continue;
                
            int tempTraversalVal= links[j]->findMaxTraversalValue(this);
            
            if (tempTraversalVal>minTraversal)
                minTraversal=tempTraversalVal;
          }
          
          traversedFromEvalFlag[i]=true;
          traversedFromVal[i]=minTraversal+1;
          return traversedFromVal[i];
          
      }   
      
      
      private:
      
      int identity;
      
      vector <node*> links;
      vector <bool>  traversedFromEvalFlag;
      vector <int>   traversedFromVal;
      
      int noOfLinks;
      node* thisNodesPtr;
      
      
        
};
 

int main()
{
    int n; // the number of adjacency relations
    vector<node*> myNodes;
    
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int xi; // the ID of a person which is adjacent to yi
        int yi; // the ID of a person which is adjacent to xi
        cin >> xi >> yi; cin.ignore();
        //cerr << xi << yi<< endl; 
        int xiNodeIndex=-1;
        int yiNodeIndex=-1;
        
        for (int j= 0; j< myNodes.size(); ++j)
        {
            if (xi==myNodes[j]->getIdentity())
                xiNodeIndex=j;
                
            if (yi==myNodes[j]->getIdentity())
                yiNodeIndex=j;
        }
        
        
        if ( (xiNodeIndex>-1) && (yiNodeIndex>-1) ) // if both nodes already preexist
        {
            myNodes[xiNodeIndex]->addLink(myNodes[yiNodeIndex]);
            myNodes[yiNodeIndex]->addLink(myNodes[xiNodeIndex]);
        }
        else if (xiNodeIndex>-1) //if only xi already preexisted
        {
            node* newNodePtr = new node(yi); 
            myNodes.push_back(newNodePtr);
            
            myNodes[xiNodeIndex]->addLink(myNodes.back());
            myNodes.back()->addLink(myNodes[xiNodeIndex]);
        }
        else if (yiNodeIndex>-1) // if only yi already preexisted
        {
            node* newNodePtr = new node(xi); 
            myNodes.push_back(newNodePtr);
            
            
            myNodes.back()->addLink(myNodes[yiNodeIndex]);
            myNodes[yiNodeIndex]->addLink(myNodes.back());
            
        }
        else // neither node preexisted
        {
           node* newNodePtr = new node(xi); 
           myNodes.push_back(newNodePtr);
            
           node* newNodePtr2 = new node(yi); 
           myNodes.push_back(newNodePtr2);
           
           myNodes[myNodes.size()-2]->addLink(myNodes[myNodes.size()-1]);
           myNodes[myNodes.size()-1]->addLink(myNodes[myNodes.size()-2]);
        }
        
        
        
        
    }  
    
    int minTime=  150000;
    for (int i=0; i<myNodes.size(); ++i)
    {
       
        
        int currentMaxTraversal;
        
        currentMaxTraversal=myNodes[i]->findMaxTraversalValue(myNodes[i]);
         if (currentMaxTraversal<minTime)
            minTime=currentMaxTraversal;
        
    }
    cout << minTime << endl; 
    
}
