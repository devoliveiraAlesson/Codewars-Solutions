def count_positives_sum_negatives(arr):
    if arr:
        positivos = [i for i in arr if i > 0]
        negativos = [i for i in arr if i < 0]
        return [len(positivos), sum(negativos)]
    else:
        return []