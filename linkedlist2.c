#include <stdio.h>
#include <stdlib.h>


struct Node{
    int data;
    struct Node* next;
};
struct Node *head;
//this insertion is at the end of the list
void Insert(int data){
    struct Node *temp1 = malloc(sizeof(struct Node));
    struct Node *temp2 = head;
    //if first node insertion, head is null and set head to first node addr. no need to change head after this.
    if (head == NULL) {

    head = temp1;
    temp1->data = data;
    temp1->next = NULL;
    return;
    }

    while (temp2->next != NULL){
        temp2 = temp2->next;
    }
    temp2->next = temp1;
    temp1->data = data;
    temp1->next = NULL;

}

void ReverseLinkedList(){
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
void recursionReverse(struct Node *p){
    if (p==NULL){
        return;
    }
    recursionReverse(p->next);
    printf("%d ", p->data);
}
void Delete(int n){
    struct Node *temp1;
    temp1 = head;

    //head is always pointing at the first node,
    //remove 1st node set head to second node if n==1
    if (n==1){
        //now head points at the second element
        head = temp1->next;
        //first element deleted
        free(temp1);
        return;
    }
    
    struct Node *temp2;
    //deleting at position other than first
    for (int i = 1; i < n - 1; i++){
        temp1 = temp1->next;
        //temp1 now points to n-1 th node.
    }
    //temp2 points to the node we want to delete.
    temp2 = temp1->next;
    temp1->next =  temp2->next;
    //delete the node
    free(temp2);

}

void Print(){
    struct Node *node;
    node = head;
    while (node != NULL){
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}

int main(){
    head = NULL; //empty list
    Insert(2);
    Insert(4);
    Insert(6);
    Insert(5);
    Insert(10);
    Insert(11);
    Insert(12);

    int n;
    // printf("enter a position: \n");
    // scanf("%d", &n);
    // Delete(n);
    Print();
    // ReverseLinkedList();
    recursionReverse(head);
}