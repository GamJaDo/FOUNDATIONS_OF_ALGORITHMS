#include <stdio.h>
#include <string.h>

int S[8] = {27, 10, 12, 20, 25, 13, 15, 22};

void merge2(int low, int mid, int high)
{
    int index;
    
    int i, j, k;
    int U[high-low];
    
    i = low;
    j = mid + 1;
    k = low;
    
    while(i<=mid && j<=high){
        if (S[i] <= S[j]) {
            U[k-low] = S[i];
            i += 1;
        }
        else{
            U[k-low] = S[j];
            j += 1;
        }
        
        k += 1;
    }
    
    if(i > mid){
        for(index=j; index<=high; index++) {
            U[k-low] = S[index];
            k += 1;
        }
    }
    else{
        for(index=i; index<=mid; index++) {
            U[k-low] = S[index];
            k += 1;
        }
    }
    
    for(index=low; index<=high; index++) {
        S[index] = U[index-low];
    }
}

void mergesort2(int low, int high)
{
    if(low < high){
        int mid = (low + high)/2;
        
        mergesort2(low, mid);
        mergesort2(mid+1, high);
        merge2(low, mid, high);
    }
}

int main(void)
{
    int i;
    
    mergesort2(0, sizeof(S)/sizeof(int) - 1);
    
    for (i = 0; i < sizeof(S)/sizeof(int); i++) {
        printf("%d ", S[i]);
    }
    
    return 0;
}

