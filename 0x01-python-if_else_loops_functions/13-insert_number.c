#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer to the linked list.
 * @number: The number to add
 * Return: adress to the newnode
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *newnode;

	newnode = malloc(sizeof(list_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;

	if (node == NULL || node->n >= number)
	{
		newnode->next = node;
		*head = newnode;
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	newnode->next = node->next;
	node->next = newnode;
	return (newnode);
}
