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
      
      vector <node*> links;
      vector <bool>  traversedFromEvalFlag;
      vector <int>   traversedFromVal;
      
      
      node(int inputIdentity) : 
            maxGenDescEvalFlag(0) , noOfLinks(0) //, maxGenAnceEvalFlag(0)
      {
              identity=inputIdentity;
              vector <node*> v(1);
              links=v;
              vector <bool> v2(1);
              traversedFromEvalFlag = v2; 
              vector <int> v3(1);
              traversedFromVal = v3;
      }
      
      
      int getIdentity()
      {
          return identity;
      }
      
      void addLink(node* linkToAdd)
      {
          if (!noOfLinks)
          {
             links[0]=linkToAdd;
             traversedFromEvalFlag[0]=false;
             traversedFromVal[0]=0;
             ++noOfLinks;
          }
          else{
          links.push_back(linkToAdd);
          traversedFromEvalFlag.push_back(false);
          traversedFromVal.push_back(0);
          ++noOfLinks;}
      }
      
      /*
      void addChild(node* childToAdd)
      {
          children.push_back(childToAdd);
      }
        
    
      node* getParent(int index)
      {
          if (index>( parents.size() - 1 ) ) // if index is out of bounds
            return nullptr;
          else
            return parents[index];
      }
    
      node* getChild(int index)
      {
          if (index>( children.size() - 1 ) ) // if index is out of bounds
            return nullptr;
          else
            return children[index];
      }
       */
       
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
          /*
          if (links.size()==1)
          {
              traversedFromEvalFlag[0]=true;
              traversedFromVal[0]=0;
              return traversedFromVal[0];
          }
          
          for (int i=0; i<links.size(); ++i)
          {
              if (links[i]==ptrOfOriginNode)
                continue;
              else if (traversedFromEvalFlag[i])
                return traversedFromVal[i];
              else
              {
                  int tempTraversalVal= links[i]->findMaxTraversalValue(this)
                  
                  traversedFromEvalFlag[0]=true;
                  traversedFromVal[0]=0;
                  return traversedFromVal[0];
                  
              }
          }*/
          
      
     /*  
      int findMaxGenerationDescendants()
      {
          if (maxGenDescEvalFlag)  // if already evald
            return maxGenerationDescendants;
          
          else if (!children.size()) //if this node has no children
          {
            maxGenDescEvalFlag = 1;
            maxGenerationDescendants=0;
            return maxGenerationDescendants;
            //return maxGenerationDescendants=0;
          }    
          else
          {
              int currentMaxGD=1;
              
              for (int i=0; i<children.size(); ++i)
              {
                int currentChildsMaxGD=  children[i]->findMaxGenerationDescendants();
                if (currentMaxGD< (currentChildsMaxGD + 1 )  )
                    currentMaxGD = (currentChildsMaxGD + 1 );
              }
              
              maxGenDescEvalFlag = 1;
            maxGenerationDescendants=currentMaxGD;
            return maxGenerationDescendants;
              //return maxGenerationDescendants=currentMaxGD;
          }
      } */
      
      /*
      int findMaxGenerationAncestors()
      {
          if (maxGenAnceEvalFlag)  // if already evald
            return maxGenerationAncestors;
          
          else if (!parents.size()) //if this node has no parents
          {
            maxGenAnceEvalFlag = 1;
            maxGenerationAncestors=0;
            return maxGenerationAncestors;
           // return maxGenerationAncestors=0;
          }
          else
          {
              int currentMaxGA=1;
              
              for (int i=0; i<parents.size(); ++i)
              {
                int currentParentsMaxGA=  parents[i]->findMaxGenerationAncestors();
                if (currentMaxGA< (currentParentsMaxGA + 1 )  )
                    currentMaxGA = (currentParentsMaxGA + 1 );
              }
              
              maxGenAnceEvalFlag = 1;
              maxGenerationAncestors=currentMaxGA;
              return maxGenerationAncestors;
              //return maxGenerationAncestors=currentMaxGA;
          }
      } */
      
      void setThisNodesPtr(node* inptPtr)
      {
          thisNodesPtr=inptPtr;
      }
      
      node* getThisNodesPtr()
      {
          return thisNodesPtr;
      }
     
      private:
      
      int identity;
      
      int maxGenDescEvalFlag;
      int maxGenerationDescendants;
      int noOfLinks;
      node* thisNodesPtr;
      //int maxGenAnceEvalFlag;
      
      //int maxGenerationAncestors;
      
      
      //vector <node*> children;
    
     
      
        
};
 

int main()
{
    int n; // the number of adjacency relations
    int minTime=  150000;
    vector<node*> myNodes;
    
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int xi; // the ID of a person which is adjacent to yi
        int yi; // the ID of a person which is adjacent to xi
        cin >> xi >> yi; cin.ignore();
        cerr << xi << yi<< endl; 
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
            newNodePtr->setThisNodesPtr(newNodePtr);
            myNodes.push_back(newNodePtr);
            
            myNodes[xiNodeIndex]->addLink(myNodes.back());
            myNodes.back()->addLink(myNodes[xiNodeIndex]);
        }
        else if (yiNodeIndex>-1) // if only yi already preexisted
        {
            node* newNodePtr = new node(xi); 
            newNodePtr->setThisNodesPtr(newNodePtr);
            myNodes.push_back(newNodePtr);
            
            
            myNodes.back()->addLink(myNodes[yiNodeIndex]);
            myNodes[yiNodeIndex]->addLink(myNodes.back());
            
        }
        else // neither node preexisted
        {
           node* newNodePtr = new node(xi); 
           newNodePtr->setThisNodesPtr(newNodePtr);
           myNodes.push_back(newNodePtr);
            
           node* newNodePtr2 = new node(yi); 
           newNodePtr2->setThisNodesPtr(newNodePtr2);
           myNodes.push_back(newNodePtr2);
           
           myNodes[myNodes.size()-2]->addLink(myNodes[myNodes.size()-1]);
           myNodes[myNodes.size()-1]->addLink(myNodes[myNodes.size()-2]);
        }
        
        
        if (i==n-1)
        {
                   // int minTime=  150000;
            
            for (int i=0; i<myNodes.size(); ++i)
          //  cerr << myNodes[i].getIdentity() << endl; 
            
            
            
            for (int i=0; i<myNodes.size(); ++i)
            {
               // int currentMinTime;
                
                int currentMaxTraversal;
                
                currentMaxTraversal=myNodes[i]->findMaxTraversalValue(myNodes[i]);
                //currentMaxAnce=myNodes[i]->findMaxGenerationAncestors();
                
              //  (currentMaxDesc>currentMaxAnce)?currentMinTime=currentMaxDesc:currentMinTime=currentMaxAnce;
                if (currentMaxTraversal<minTime)
                    minTime=currentMaxTraversal;
                
            }
        }
        
    }  
        
        /*
        if ( (xiNodeIndex>-1) && (yiNodeIndex>-1) ) // if both nodes already preexist
        {
            myNodes[xiNodeIndex].addChild(&myNodes[yiNodeIndex]);
            myNodes[yiNodeIndex].addParent(&myNodes[xiNodeIndex]);
        }
        else if (xiNodeIndex>-1) //if only xi already preexisted
        {
            myNodes.push_back(node(yi));
            
            myNodes[xiNodeIndex].addChild(&myNodes.back());
            myNodes.back().addParent(&myNodes[xiNodeIndex]);
        }
        else if (yiNodeIndex>-1) // if only yi already preexisted
        {
            myNodes.push_back(node(xi));
            
            myNodes.back() . addChild(&myNodes[yiNodeIndex]);
            myNodes[yiNodeIndex].addParent(&myNodes.back());
            
        }
        else // neither node preexisted
        {
           myNodes.push_back(node(xi));
           myNodes.push_back(node(yi));
           
           myNodes[myNodes.size()-2].addChild(&myNodes[myNodes.size()-1]);
           myNodes[myNodes.size()-1].addParent(&myNodes[myNodes.size()-2]);
        }
       */ 
       
       /*
    for(int k=0; k<myNodes.size(); ++k)   { 
    for (int i=0; i<myNodes[k]->links.size(); ++i)
    {
        cerr<< static_cast<void*>(myNodes[k]->links[i]) << endl;
    }
    } */
    /*
    int minTime=  150000;
    
    for (int i=0; i<myNodes.size(); ++i)
  //  cerr << myNodes[i].getIdentity() << endl; 
    
    
    
    for (int i=0; i<myNodes.size(); ++i)
    {
       // int currentMinTime;
        
        int currentMaxTraversal;
        
        currentMaxTraversal=myNodes[i]->findMaxTraversalValue(myNodes[i]);
        //currentMaxAnce=myNodes[i]->findMaxGenerationAncestors();
        
      //  (currentMaxDesc>currentMaxAnce)?currentMinTime=currentMaxDesc:currentMinTime=currentMaxAnce;
        if (currentMaxTraversal<minTime)
            minTime=currentMaxTraversal;
        
    }*/
    
    // Write an action using cout. DON'T FORGET THE "<< endl"
    // To debug: cerr << "Debug messages..." << endl;


    // The minimal amount of steps required to completely propagate the advertisement
    cout << minTime << endl; 
    
}
