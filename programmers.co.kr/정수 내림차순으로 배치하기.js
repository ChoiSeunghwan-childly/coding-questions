function solution(n) {
    return n.toString().split('').map( n => Number(n) ).sort( (a,b) => b-a).join('')-0;
}
