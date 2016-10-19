def grader(urls, target):
    score = 0
    for i in range(10):
        try:
            if urls[i] == target:
                score = 10 - i
                break
        except:
            break
    return score
