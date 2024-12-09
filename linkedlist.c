#include <stdio.h>
#include <stdlib.h>

struct Node{
    int data;
    struct Node* next;
};

struct Node* head;

int main(){
    head = NULL; //the list is empty
    

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