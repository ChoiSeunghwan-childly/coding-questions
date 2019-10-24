function solution(array, commands) {
    let answer = [];    
    commands.forEach( (item) =>{
        let [i, j, k ]= item;
        answer.push( array.slice(i-1, j).sort( (a,b) => a-b )[k-1] );
    })    
    return answer;
}