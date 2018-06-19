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

// delete linked lists
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

  assert(toPop != nullptr);
  
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


// Given list A and B, append B to end of A
void append(Node* &headrefA, Node* &headrefB)
{
  // if A empty, reset reference to B
  if (headrefA == nullptr)
  {
    headrefA = headrefB;
    headrefB = nullptr;
    return;
  }

  // if B empty, do nothing
  if (headrefB == nullptr)
  {
    return;
  }

  // iterate over A till reach end and then attach B
  Node* curr = headrefA;
  while(curr->next != nullptr)
  {
    curr = curr->next;
  }

  curr->next = headrefB;
  headrefB = nullptr;

  return;

}

// Split a list.  If odd number of elements, then goes to the first list
void frontBackSplit(Node* sourceref, Node* &frontref, Node* &backref)
{

  frontref = sourceref;
  
  // if source list is empty or if only has 1 node
  if ( (sourceref == nullptr) || (sourceref->next == nullptr) )
  {
    backref = nullptr;
    return;
  }

  // use slow and fast pointer to identify midpoint
  Node* sptr = sourceref;
  Node* fptr = sourceref -> next;

  while (fptr != nullptr)
  {

    fptr = fptr -> next;
    
    if (fptr != nullptr)
    {
      fptr = fptr -> next;
      sptr = sptr -> next;
    }
    
  }

  backref = sptr->next;
  sptr -> next = nullptr;

  return;
  
}

// take 2 lists, removes from node from second list and pushes it onto front of the first
void moveNode(Node* &aref, Node* &bref)
{
  // edge case of b being empty
  if (bref == nullptr)
  {
    return;
  }

  Node* dummy = bref->next;

  bref->next = aref;
  aref = bref;

  bref = dummy;

}

// take 2 lists in sorted increasing order
// and merge them into one sorted list
Node* sortedMerge(Node* &aref, Node* &bref)
{
  Node dummy;
  dummy.next = nullptr;
  Node* tail = &dummy;

  while (1)
  {
    // if a is empty
    if (aref == nullptr)
    {
      tail->next = bref;
      break;
    }
    else if (bref == nullptr)
    {
      tail->next = aref;
      break;
    }
    // neither a nor b are empty
    else
    {
      if (aref->data < bref->data)
      {
	moveNode(tail->next, aref);
      }
      else
      {
	moveNode(tail->next, bref);
      }
      tail = tail->next;
    }
      
  } // end while

  return dummy.next;
}

// given list, split into two smaller lists, recursively sort those lists
// and merge two sorted lists back together
void mergeSort(Node* &headref)
{
  Node* head = headref;
  Node* left;
  Node* right;

  // base case of no more need to split
  // 0 or 1 length
  if ( (head == nullptr) || (head->next == nullptr) )
  {
    return;
  }

  // use frontBackSplit and sortedMerge
  // split list into 2
  frontBackSplit(head, left, right);
  
  mergeSort(left);
  mergeSort(right);

  headref = sortedMerge(left, right);
  
}

// given two lists sorted in increasing order, create and return a new list representing
// intersection of the two lists new list should be made with its own memory,
// i.e. original lists should not be changed.  This should be done with push()
// list building rather than moveNode.
// ignores duplicates
Node* sortedIntersect(Node* refA, Node* refB)
{

  Node dummy;
  dummy.next = nullptr;
  Node* head = &dummy;
  
  //(Node* &headref, int data)

  // keep iterating until either A or B is empty
  while ( (refA != nullptr) && (refB != nullptr) )
  {
    // compare, 3 cases
    // (1) equal
    // (2) A > B -- advance B
    // (3) A < B -- advance A
    if (refA->data == refB->data)
    {
      push(head->next, refA->data);
      head = head->next;
      refA = refA -> next;
      refB = refB -> next;
    }
    else if (refA->data > refB->data)
    {
      refB = refB->next;
    }
    else
    {
      refA = refA->next;
    }
  }
  
  return dummy.next;
  
}


// iterative reverse function that reverses a list by rearranging
// all the .next pointers and the head pointer
void reverse_list_iter(Node* &headref)
{
  Node* prev = nullptr;
  Node* curr = headref;
  Node* next;

  while (curr != nullptr)
  {
    next = curr->next;
    curr->next = prev;
    prev = curr;
    curr = next;
    //next = curr->next;
  }

  headref = prev;
}

// reverse recursive
void reverse(Node* &headref)
{
  if (headref == nullptr)
  {
    return;
  }

  Node* first;
  Node* rest;

  first = headref;
  rest = first->next;

  if (rest == nullptr)
  {
    return;
  }
  
  reverse(rest);

  first->next->next = first;
  first->next = nullptr;
  
  headref = rest;
}

// given node, insert into correct sorted position
void sortedInsert(Node* &headref, Node* nNode)
{
  // edge case of empty list or if node should be inserted at the front
  if ( (headref == nullptr) || (headref->data >= nNode->data) )
  {
    nNode->next = headref;
    headref = nNode;
    return;
  }
  
  Node* curr = headref;

  while ( (curr->next != nullptr) && (curr->next->data < nNode->data) )
  {
    curr = curr->next;
  }

  nNode->next = curr->next;
  curr->next = nNode;
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

  std::cout << "Length of list is " << length(list1) << std::endl;

  std::cout << "Number of 3s " << count(list1, 3) << std::endl;
  std::cout << "Number of 8s " << count(list1, 8) << std::endl;

  std::cout << "Getting 3rd element of list " << getNth(list1, 3) << std::endl;

  insertNth(list1, 3, 2);

  std::cout << "Inserted 3 into the 2nd position" << std::endl;
  
  printList(list1);

  Node* toInsert = newNode(7);
 
  sortedInsert(list1, toInsert);

  std::cout << "Inserted 7" << std::endl;

  printList(list1);

  int values2[] = {8, 9, 10, 11, 12};

  Node* list2 = createList(values2, 5);

  printList(list2);

  append(list1, list2);

  printList(list1);

  std::cout << "Spliting list into two" << std::endl;
  
  Node* front;
  Node* back;
  
  frontBackSplit(list1, front, back);

  printList(front);
  printList(back);

  std::cout << "Moved first node of back list to front of front list" << std::endl;
  moveNode(front, back);
  printList(front);
  printList(back);

  std::cout << "Popping out first element " << pop(front) << std::endl;
  
  //sortedMerge
  Node* sortedList = sortedMerge(back, front);

  printList(sortedList);

  std::cout << "Deleting sortedList" << std::endl;
  deleteList(sortedList);

  
  int values3[] = {4, 1, 2, 9, 5, 0, 3, 1, 10};

  Node* list3 = createList(values3, 9);

  printList(list3);

  mergeSort(list3);

  std::cout << "About to test out sortedIntersect" << std::endl;

  //Testing sortedIntersect
  int values4[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  for (int i = 0; i < 10; ++i)
  {
    std::cout << values4[i] << " ";
    
  }
  std::cout << std::endl;
  
  Node* list4 = createList(values4, 10);

  printList(list4);
  
  int values5[] = {2, 4, 6, 8, 10};
  Node* list5 = createList(values5, 5);

  printList(list5);
  
  Node* intersect = sortedIntersect(list4, list5);

  printList(intersect);

  reverse_list_iter(intersect);

  printList(intersect);

  reverse(intersect);

  printList(intersect);
  
  deleteList(list3);
  deleteList(list4);
  deleteList(list5);
  deleteList(intersect);

}
