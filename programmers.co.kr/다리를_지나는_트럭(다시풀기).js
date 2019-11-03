function solution(bridge_length, weight, truck_weights) {
    // 잘못 풀었다... 생각해보니 무게별로 다리를 건너다가 먼저 빠져나간
    // 트럭도 있는 등의 상황을 생각 못함.
    // 큐로 풀어야 될 듯.
    // for timeticker 돌리면서.
    
    let sec = 0;
    
    while(truck_weights.length){
        let capacity = weight;
        let on_trucks = [];
        for(let i = 0; i < truck_weights.length; i++){
            if (capacity === 0)
                break;
            
            if (truck_weights[i] <= capacity){
                on_trucks.push(truck_weights[i]);
                truck_weights.splice(i,1);
                i -= 1
            }
        }
        sec += bridge_length; 
    }
    return sec;
}
