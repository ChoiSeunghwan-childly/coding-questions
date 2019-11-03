function solution(strings, n) {
    const copy = strings.concat();
    copy.sort( (a,b) => {
        // console.log(a, b, n);
        if (a[n] === b[n])
            return a < b ? -1 : 1;
        else
            return a[n] < b[n] ? -1 : 1;
    });
    // console.log(copy);
    return copy;
}
