#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a node to a sorted singly linked list
 * @head: the head of the list
 * @number: the number beig added
 * Return: returns the address the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = *head;
	listint_t *new = malloc(sizeof(listint_t));
	listint_t *prev = NULL;

	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (tmp == NULL)
	{
		tmp = new;
		return (new);
	}

	while (tmp)
	{
		if (tmp->n > number)
		{
			new->next = tmp;
			if (prev)
				prev->next = new;
			return (new);
		}
		prev = tmp;
		tmp = tmp->next;
	}
	if (!tmp)
		prev->next = new;

	return (new);
}
