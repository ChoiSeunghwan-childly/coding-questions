function solution(bridge_length, weight, truck_weights) {
    let sec = 0;
    const bridge_q = [];    
    let capacity = weight;
    
    while(truck_weights.length || bridge_q.length){
        sec += 1
        
         //process
        for(let i = 0; i < bridge_q.length; i++)
            bridge_q[i].distance -= 1;
               
        //dequeue
        if(bridge_q[0])
            if(bridge_q[0].distance <= 0){
                capacity += bridge_q[0].weight;
                bridge_q.shift();
                
                if(capacity > weight)
                    return "err";
            }
        
        //enqueue
        if(truck_weights[0])
            if(truck_weights[0] <= capacity){
                capacity -= truck_weights[0];
                bridge_q.push({distance: bridge_length, 
                weight: truck_weights.shift()});     
                
                if(capacity < 0 )
                    return "capaErr";
            }
       
    }
    return sec;
}
