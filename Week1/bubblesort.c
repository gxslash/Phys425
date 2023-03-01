#include <stdio.h>
#include <time.h>
#include <stdlib.h>

void swap(double *xp, double *yp){
    double temp = *xp;
    *xp = *yp;
    *yp = temp;
}


void bubble_sort(double arr[], size_t n)
{
    for (size_t i = 0; i < n-1; i++)
        for (size_t j = 0; j < n-i-1; j++)
            if (arr[j] > arr[j+1])
                swap(&arr[j], &arr[j+1]);    
}

double calculate_time(double *arr, size_t len) {
    double time_spent = 0.0;
    clock_t begin = clock();
    bubble_sort(arr, len);
    clock_t end = clock();
    time_spent += (double)(end - begin) / CLOCKS_PER_SEC;
    return time_spent;
}


double **generate_random_matrix(size_t rows) {
    double **rand_mat = (double **)malloc(rows * sizeof(double*));
    if(!rand_mat)
    {   
        printf("Problem got here");
        return NULL;
    }

    for (size_t row = 0; row < rows; row++)
    {
        size_t cols = 100*row;
        rand_mat[row] = (double *)malloc(cols * sizeof(double));
        for (int col = 0; col < cols; col++)
        {
            rand_mat[row][col]=rand()%cols;
        }
    }
    
    return rand_mat;
}


int main(void) {

    size_t counts = 100;
    double **rand_mat = generate_random_matrix(counts);

    double times[counts];

    double time_spent = 0.0;
    clock_t begin = clock();
    for (size_t row = 1; row < counts; row++)
    {
        times[row] = calculate_time(rand_mat[row], 100*row);
    }
    clock_t end = clock();
    time_spent += (double)(end - begin) / CLOCKS_PER_SEC;

    for (size_t i = 0; i < counts; i++)
        printf("time[%d] is %f\n", i, times[i]);

    printf("Total time to execute: %f", time_spent);
    
    for (size_t row = 0; row < counts; row++)
    {
        free(rand_mat[row]);
    }
    free(rand_mat);

    return 0;
}