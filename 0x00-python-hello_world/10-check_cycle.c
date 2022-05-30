#include "lists.h"

/**
 * check_cycle - check cycle
 * @list: list to check
 * Return: 0 no cysle else 1
 */

int check_cycle(listint_t *list)
{
	listint_t *now;

	if (list == NULL)
		return (0);

	now = list->next;

	while (now != NULL)
	{
		if (now == list)
			return (1);
		now = now->next;
	}

	return (0);
}
