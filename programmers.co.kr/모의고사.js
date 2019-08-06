function solution(answers) {
    let answer = [];
    let p1 = [1, 2, 3, 4, 5];
    let p2 = [2, 1, 2, 3, 2, 4, 2 , 5]
    let p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]    
    let score_p1 = 0, score_p2 = 0, score_p3 = 0;

    for (let idx in answers){
        if(p1[idx % p1.length] === answers[idx])
            score_p1 += 1;
        if(p2[idx % p2.length] === answers[idx])
            score_p2 += 1;
        if(p3[idx % p3.length] === answers[idx])
            score_p3 += 1;
    }
    let maxNum = Math.max(score_p1, score_p2, score_p3);

    if (score_p1 === maxNum) { answer.push(1)};
    if (score_p2 === maxNum) { answer.push(2)};
    if (score_p3 === maxNum) { answer.push(3)};

    return answer;
}
