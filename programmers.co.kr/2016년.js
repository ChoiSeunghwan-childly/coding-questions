function solution(a, b) {
    let answer = '';
    const days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    const yoil = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];

    let day = 0;
    for(let i = 0; i < a - 1; i++)
        day += days[i];
    day += b -1 + 5;

    answer = yoil[day % 7];

    return answer;
}