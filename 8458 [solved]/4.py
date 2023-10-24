with open('input.txt', 'r') as r, open('output.txt', 'w') as w:
    read = lambda: r.readline()
    write = lambda text: w.write(f'{text}\n')

    k = int(read()) * 2
    cnt = i = 0
    brackets = ['' for _ in range(k)]


    def generate(cnt, i, k, brackets):
        if cnt <= k - i - 2:
            brackets[i] = '('
            generate(cnt + 1, i + 1, k, brackets)
        if cnt > 0:
            brackets[i] = ')'
            generate(cnt - 1, i + 1, k, brackets)
        if k == i and cnt == 0:
            s = ''.join(brackets)
            write(s)

    generate(cnt, i, k, brackets)