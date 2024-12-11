//reversing a linked list
#include <stdio.h>
#include <stdlib.h>


struct Node{
    int data;
    //read it as next is a pointer to a struct Node
    struct Node *next;
};

struct Node *head;

void reversePrint(struct Node *p){
    if (p==NULL){
        return;
    }
    reversePrint(p->next);
    printf("%d ", p->data);
}

void reverseLinkedList(){
    struct Node *current, *prev, *next;
    current = head;
    prev = NULL; //because prev is NULL for the first node after reversal
    while (current != NULL){
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }
    head = prev;
}


int main(){
    head = NULL;
    //say linked list looks like this, address neglected
    // Head -> 2 -> 4 -> 6 -> 8 -> NULL
    // Reversed Head -> 8 -> 6 -> 4 -> 2 -> NULL
    //we always have head so assume it


    //call to the function
    reversePrint(head);
    // reverseLinkedList();
    



    return 0;
}