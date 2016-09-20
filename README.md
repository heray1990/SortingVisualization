# AlgorithmVisualization

## Table of Contents

- [Bubble Sort](https://github.com/heray1990/AlgorithmVisualization#bubble-sort)

## Bubble Sort

As "Introduction to Algorithms" introduces, _Bubblesort is a popular, but inefficient, sorting algorithm. **It works by repeatedly swapping adjacent elements that are out of order**_.

```
BUBBLESORT(A)
1 for i = 1 to A.length - 1
2     for j = A.length downto i + 1
3         if A[j] < A[j - 1]
4             exchange A[j] with A[j - 1]
```

Download [src/visual_bubble_sort.py](https://github.com/heray1990/AlgorithmVisualization/blob/master/src/visual_bubble_sort.py) and run it in Linux. You will intuitively see how bubble sort works.

Run the command `python visual_bubble_sort.py 50`, you will get the animation as follow.

![bubble_sort_50samples_fps20_dpi50](https://raw.githubusercontent.com/heray1990/AlgorithmVisualization/master/images/bubble_sort_50samples_fps30_dpi50.gif)
