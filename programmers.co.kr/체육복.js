function solution(n, lost, reserve) {
    var answer = 0;
    answer = n - lost.length;

    for(let i = 0; i < lost.length; i++){
        if(reserve.indexOf(lost[i]) !== -1 ){
            reserve[reserve.indexOf(lost[i])] = -9;
            lost[i] = -3;
            answer += 1;
        }
    }

    for (let i = 0; i < lost.length; i++) {
        let lo = lost[i];

        if (reserve.indexOf(lo - 1) !== -1) {
            reserve[reserve.indexOf(lo - 1)] = -9;
            answer += 1;
        }
        else if (reserve.indexOf(lo + 1) !== -1) {
            reserve[reserve.indexOf(lo + 1)] = -9;
            answer += 1;
        }
    }

    return answer;
}

let num = solution(3, [1, 2], [2, 3]);
console.log(num);


// TESTCASE 아래 3개 통과되면 되는듯합니다.

// n = 3, lost = [1,2], reserve = [2,3]
// answer : 2

// n = 9 , lost = {2,4,7,8 }, reserve = {3,6,9}
// answer = 8

// n = 5, lost = {2,4}, reserve = {3,5}
// answer = 5