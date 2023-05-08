#include "lists.h"

/**
 * check_cycle - checks for a linked list
 * @list: linked list
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *snail = list;
	listint_t *flash = list;

	if (list == NULL)
		return (0);
	while (snail && flash && flash->next)
	{
		snail = snail->next;
		flash = flash->next->next;
		if (snail == flash)
			return (1);
	}
	return (0);
}
