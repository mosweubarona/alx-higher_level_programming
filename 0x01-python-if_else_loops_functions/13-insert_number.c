#include "lists.h"
#include <stdlib.h>

/**
 * insert_node -  inserts a number into a sorted singly linked list
 * @head: singly list head
 * @number: number to insert
 * Return: the address of the updated node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *updated;
	listint_t *current;

	current = *head;

	updated = malloc(sizeof(listint_t));
	if (updated == NULL)
		return (NULL);

	updated->n = number;

	if (*head == NULL)
		*head = updated;
	else
	{
		while (current->next != NULL)
		{
			if (current->next->n > number)
				break;

			current = current->next;
		}
		updated->next = current->next;
		current->next = updated;
	}

	return (updated);
}
