#include <stdio.h>
    int prev = 0, current = 1, next;
    printf("\nFibonacci Sequence up to 100:\n");
    printf("%d, %d, ", prev, current);
    while ((next = prev + current) <= 100) {
        printf("%d, ", next);
        prev = current;
        current = next;
    }
    printf("\n");

 