#include "lists.h"
/**
* check_cycle - check linked list for cycle
* @list: pointer to head node
* Return: 1 if cycle, 0 if no cycle
*/ 

int check_cycle(listint_t *list)
{
	listint_t *head_copy = list;

	if(list == NULL)
	{
		return (0); }
	while(list->next != NULL)
	{
		if(list->next == head_copy)
			return(1);

		list = list->next; }
	return (0);

}
