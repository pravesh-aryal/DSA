//inserting at the nth position
#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    struct Node *next;
};
//head pointer;
struct Node *head;

//index starts at n = 1,2,3,4,5 there are no zeros
void Insert(int data, int n){
    struct Node *temp1 = malloc(sizeof(struct Node));
    temp1->data = data;
    //head is NULL at first and then is updated.
    temp1->next = NULL;
    if (n == 1){
        temp1->next = head;
        head = temp1;
        return;
    }
    //if inserting somewhere else other than 1 loop until to get the n-1th node
    struct Node *temp2 = head;
    for (int i = 0; i < n-2; i++){
        temp2 = temp2->next;
    }
    temp1->next = temp2->next;
    temp2->next = temp1;
    
}

void Print(){
    struct Node *node = head;
    while (node != NULL){
        printf("%d    ", node->data);
        node = node->next;
    }

}

int main(){
    head = NULL;
    Insert(2,1);
    Insert(3,2);
    Insert(4,1);
    Insert(5,2);
    Insert(69, 1);
    Print();
}






















// #include <stdio.h>
// #include <stdlib.h>
// //requirements, nodes inserted at the beginning everytime and print it.
// struct Node{
//     int data;
//     struct Node* next;
// };

// struct Node* head;

// void Insert(int x){
//     struct Node* temp = malloc(sizeof(struct Node));
//     temp->data = x;
//     temp->next = head;
//     head = temp;
// }

// void Print(){
//     //print the linkedlist
//     struct Node* nodePtr = head;
//     while (nodePtr != NULL){
//         printf("%d ", nodePtr->data);
//         nodePtr = nodePtr->next;
//     }
// }


// int main(){
//     head = NULL; //the list is empty initially
//     printf("Enter number of items: \n");
//     int n, x;
//     scanf("%d", &n);
//     for (int i = 0; i < n; i++){
//         printf("\nHEAD IS %p", head);
//         printf("Enter the data number: \n");
//         scanf("%d", &x);
//         //defined by me
//         Insert(x);
//         printf("---printing--- \n");

//         Print();
//         //
//     }
 
// }


// //inserting and traversing
// #include <stdio.h>
// #include <stdlib.h>


// int main(){

//     struct Node{
//         int data;
//         struct Node* link;
//     };
//     struct Node* A;
//     A = NULL; //A points nowhere //just a head pointer pointing to the first node

//     //create a node, a memory block, malloc

//     struct Node* temp = malloc(sizeof(struct Node)); //created pointer to one node.
//     (*temp).data = 2;
//     // temp->data = 2;
//     // temp->link = NULL;
//     (*temp).link = NULL; //now its the last node.
//     A = temp;
// }
