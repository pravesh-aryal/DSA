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

//two pointers approach for removing Nth from end
void removeNthNodeFromEnd(Node*& head, int n){
    //1,2,3,4,5
    Node* fast = head;
    Node* slow;
    Node* previous;
    slow = head;
    //fast is n steps ahead
    for (int i = 1; i <=n; i++){
        fast = fast->next;
    }
    
    //if its first node i.e fast = NULL
    if (!fast){
        head = head->next;
        return;
    }
    

    //fast will be n steps ahead
    while (fast){
        cout <<"previous " << previous->data << " Slow " << slow->data << "Fast" << fast->data << endl; 
        fast = fast->next;
        //slow is the current node from which we want a link which is set to previous
        previous = slow;
        slow = slow->next;

    }
    previous->next = slow->next;
}

void reorderLinkedList(Node*& head){
    /*
    1->2->3->4->5 
    1->5->2->4->3

    1,2,3,4,5
    Transition: 1->next = 5, 5->next = 2, 4->next = nullptr;
    //variable usage: lastNode = 5, secondLastNode = 4, currentNode = 1
    //at last set currentNode to 2 i.e lastNode->next;
    1,5,2,3,4
    1,5,2,4,3
    */

    Node *currentNode = head;
    Node *previousNode = nullptr;
    Node *nextNode = head->next;
    Node *lastNode;
    Node *secondLastNode;

    if (!nextNode || !nextNode->next){
        //if there is no next node return i.e only 1 node
        return;
    }
    while(currentNode->next){ // 2, 3, 4, 5, nullptr
        while (nextNode->next){ //3, 4, 5
            if (!nextNode->next->next){
                secondLastNode = nextNode;
            }

            nextNode = nextNode->next;

        }
        //after the loop is done we have the last node in nextNode
        lastNode = nextNode; //5
        secondLastNode->next = nullptr;; //4
        lastNode->next = currentNode->next; //5->2
        currentNode->next = lastNode; //1->5
    
        currentNode = lastNode->next;
        //this should continue until my currentNode's direct next is null.
    }

}

//void removeNthNodeFromEnd(Node*& head, int n){
//    //1,2,3,4,5
//    //the length approach
//    Node* currentNode = head;
//    int length = 0;
//    while (currentNode){
//        currentNode = currentNode->next;
//        length++;
//    }
//    int deletionIndex;
//    deletionIndex = length - n + 1;
//    Node* previousNode;
//    currentNode = head;
//    Node* nextNode;
//    //if it first node
//    if (n == 1){
//        head = head->next;
//    }
//
//    //if nth node, let n = 3
//    for (int i = 2; i <= deletionIndex; i++){
//        previousNode = currentNode; //1, 2, 
//        currentNode = currentNode->next; //2, 3, 
//        // nextNode = currentNode->next;
//
//        if ( i == deletionIndex){
//            previousNode->next = currentNode->next;
//        }
//
//    } 
//}

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
    // append(head, 5);

    cout << "The current unchanged linkedlist looks like: \n" << endl;
    printList(head);

    // reverseLinkedList(head);
    // removeNthNodeFromStart(head, 5);
    // removeNthNodeFromEnd(head, 2); //1,2,3,4,5
    reorderLinkedList(head);

    cout << "Reordered linkedlist " << endl;
    printList(head);
}

