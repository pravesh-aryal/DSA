#include <stdio.h>
#include <stdlib.h>
//requirements, nodes inserted at the beginning everytime and print it.
struct Node{
    int data;
    struct Node* next;
};

struct Node* head;

void Insert(int x){
    struct Node* temp = malloc(sizeof(struct Node));
    temp->data = x;
    temp->next = head;
    head = temp;
}

void Print(){
    //print the linkedlist
    struct Node* nodePtr = head;
    while (nodePtr != NULL){
        printf("%d ", nodePtr->data);
        nodePtr = nodePtr->next;
    }
}


int main(){
    head = NULL; //the list is empty initially
    printf("Enter number of items: \n");
    int n, x;
    scanf("%d", &n);
    for (int i = 0; i < n; i++){
        printf("Enter the data number: \n");
        scanf("%d", &x);
        //defined by me
        Insert(x);
        printf("---printing--- \n");
        Print();
        //
    }
}


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