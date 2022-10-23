import java.util.Arrays;

class index {

    private static void bubbleSort(int[] arr, String direction) {
        boolean noMoreSwaps = false;
        int n = 1;
        while (!noMoreSwaps) {
            noMoreSwaps = true;
            for (int i = 0; i < arr.length - n; i++) {
                if (direction == "asc" ? arr[i] > arr[i + 1] : arr[i] < arr[i + 1]) {
                    int temp = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = temp;
                    noMoreSwaps = false;
                }
            }
            n++;
        }
    }

    public static void sort(int[] arr) {
        bubbleSort(arr, "asc");
    }

    public static void sort(int[] arr, String direction) {
        bubbleSort(arr, direction);
    }

    public static void main(String[] args) {
        int arr[] = { 3, 4, 5, 6, 2, 3, 1, 98, 4, 324, 13, 2, 3 };
        sort(arr, "desc");
        System.out.println("Sorted array --> " + Arrays.toString(arr));
    }
}