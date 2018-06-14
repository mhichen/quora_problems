#include<iostream>
#include <stdlib.h>
#include <cassert>

struct Node
{
  // integer data
  int data;

  // pointer to next node
  struct Node* next;
  
};
  

struct Node* newNode(int key)
{
  Node* newNode = new Node;

  newNode -> data = key;
    
  newNode -> next = nullptr;
  
};


// push -- add node to head of a list
void push(Node* &headref, int data)
{
  Node* dummy = newNode(data);

  dummy -> next = headref;

  headref = dummy;
  
}

// createList
Node* createList(int vals[], int n)
{

  Node* head = nullptr;

  for (int i = n - 1; i >= 0; --i)
  {
    push(head, vals[i]);
  }

  return head;

}

// print list
void printList(Node* headref)
{
  Node* curr = headref;

  while (curr != nullptr)
  {
    std::cout << curr->data << " ";
    curr = curr->next;
  }
  std::cout << std::endl;
  
}

// append to end of list appendNode
void appendNode(Node* &headref, int val)
{
  Node* newnode = newNode(val);

  Node* curr = headref;

  // special case of length 0 linked list
  if (curr == nullptr)
  {
    headref = newnode;
  }
  else
  {
    while (curr -> next != nullptr)
    {
      curr = curr -> next;
    }
  }

  curr -> next = newnode;

}

// clone given linked list

// count length of linked list
int length(Node* headref)
{
  int count = 0;

  while (headref != nullptr)
  {
    ++count;
    headref = headref -> next;
  }

  return count;
  
}

// count number of times a given int occurs in a list
int count(Node* headref, int val)
{
  int count = 0;

  while (headref != nullptr)
  {
    if (headref -> data == val)
    {
      ++count;
    }

    headref = headref -> next;
  }

  return count;
  
}

// get value stored at index N
int getNth(Node* headref, int n)
{
  Node* curr = headref;
  int count = 0;

  while (curr != nullptr)
  {
    if (count == n)
    {
      return curr -> data;
    }

    ++count;
    curr = curr -> next;
    
  }

  assert(0); // reach here if asking for non-existent value
  
}

// delete linked list
void deleteList(Node* &headref)
{
  Node* curr = headref;
  Node* next;

  while (curr != nullptr)
  {
    next = curr -> next;

    delete curr;

    curr = next;
    
  }

  headref = nullptr;
  
}

// remove first element in list and return value
int pop(Node* &headref)
{
  int val;
  Node* toPop = headref;

  assert(toPop != nullptr)
  
  headref = headref -> next;
  
  val = toPop->data;

  delete toPop;

  return val;
}

// insert value into n-th index spot
void insertNth(Node* &headref, int data, int n)
{
  if (n == 0)
  {
    push(headref, data);
    return;
  }

  Node* curr = headref;

  int count = 0;
  
  while (curr != nullptr)
  {
    if (count == (n - 1))
    {
      push(curr->next, data);
      return;
    }

    ++count;
    curr = curr->next;
  }

  assert(0);
  
}

// given sorted linked list, insert node into correct position
void sortedInsert(Node* &headref, Node* newNode)
{
  if ( (headref == nullptr) || (headref -> data >= newNode -> data) )
  {
    newNode->next = headref;
    headref = newNode;
    return;
  }

  Node* curr = headref;

  while (curr->next != nullptr && curr->next->data < newNode->data)
  {
    curr = curr->next;
  }

  newNode->next = curr->next;
  curr->next = newNode;
  
  return;
}

int main()
{

  int values1[] = {1, 2, 3, 4, 5};

  Node* list1 = createList(values1, 5);

  printList(list1);

  appendNode(list1, 6);
  
  printList(list1);

  std::cout << "Popping " << pop(list1)  << std::endl;

  printList(list1);

  std::cout << length(list1) << std::endl;

  std::cout << count(list1, 3) << std::endl;
  std::cout << count(list1, 8) << std::endl;

  std::cout << getNth(list1, 3) << std::endl;
  //std::cout << getNth(list1, 8) << std::endl;

  std::cout << "Deleting list" << std::endl;
  deleteList(list1);

  std::cout << length(list1) << std::endl;

  
  
}
