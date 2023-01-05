#include "lists.h"
#include <stdio.h>

/**
 * insert_node - function in C that inserts a number 
 * into a sorted singly linked list
 * @head: pointer to the singly linked list
 * @number: number to insert in to new node
 * Return: the address to the new node, NULL if fails
 */

listint_t *insert_node(listint_t **head, int number)
{
listint_t *new = NULL;
listint_t *current = NULL;
listint_t = current = *head;
if (!head)
	return (NULL);
 new = malloc(sizeof(listint_t));
 if (!new)
	 return (NULL);
 new->n =  number;
 new->next = NULL;
 if (!*head || (*head->n) > number)
 {
	 new->next = *head;
	 return (*head = new);
 }
 else
 {
	 while (current && current->n < number)
	 {
		 temp = current;
		 current = current->next;
	 }
	 temp->next = new;
	 new->next = current;
 }
 return (new);
}
