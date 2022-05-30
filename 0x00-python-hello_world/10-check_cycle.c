#include "lists.h"

/**
 * check_cycle - check cycle
 * @list: list to check
 * Return: 0 no cysle else 1
 */

int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *last = list;

	if (!list)
		return (0);

	while (first && last && last->next)
	{
		first = first->next;
		last = last->next->next;
		if (first == last)
			return (1);
	}

	return (0);
}
