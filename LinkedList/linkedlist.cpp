#include <iostream>
using namespace std;

struct Node{
    int data; 
    Node* next;
};

//i am getting address of the head ptr in main
void append(Node*& head, int value){
    //here head = nullptr or 0x01
    Node* newNode = new Node{value, nullptr};
    if (!head){
        head = newNode;
        return;
    }

    Node* temp = head;
    while (temp->next){
        temp = temp->next;
    }

    temp->next = newNode;
}

void printList(Node* head){
    cout << "Linked List: ";
    while (head){
        cout << head->data << " --> ";
        head = head->next;
    }
    cout << "NULL" << endl;
}

void reverseLinkedList(Node*& head){
    //for the first node, we make it point to null and break the link.
    //from the second node
    Node* previousNode = nullptr; 
    Node* currentNode = head; 
    Node* nextNode = currentNode->next;

    while (currentNode){//1 2
        nextNode = currentNode->next; //2 3
        //reverseing step
        currentNode->next = previousNode; //null, 1
        //getting it ready for next loop
        previousNode = currentNode;//1, 2
        currentNode = nextNode;
    }
    //updating the head.
    head = previousNode;

}

void removeNthNodeFromStart(Node*& head, int n){
    //1->2->3->4->5
    Node* previousNode;
    Node* currentNode = head;
    Node* nextNode;
    //if it first node
    if (n == 1){
        head = head->next;
    }

    //if nth node, let n = 3
    for (int i = 2; i <= n; i++){
        previousNode = currentNode; //1, 2, 
        currentNode = currentNode->next; //2, 3, 
        // nextNode = currentNode->next;

        if ( i == n){
            previousNode->next = currentNode->next;
        }

    }


}

int main(){
    Node* head = nullptr; //nullptr because safe.
    //address of head = 0x01 
    int n, value;
    // cout << "Enter the number of nodes you want: ";
    // cin >> n;

    // for (int i = 0; i < n; ++i){
    //     cout << "Enter data int for node" << i + 1 << ": ";
    //     cin >> value;
    //     append(head, value);
    // }
    append(head, 1);
    append(head, 2);
    append(head, 3);
    append(head, 4);
    append(head, 5);

    printList(head);

    // reverseLinkedList(head);
    removeNthNodeFromStart(head, 5);
    printList(head);
}

