function solution(p, l) {
    let ans = 0;
    
    while(p.length){
        let i = p.shift();
        
        if (i === Math.max.apply(null, p)){
            ans += 1;
            
            if (l === 0)
                break;
            else 
                l -= 1;
            
        }else{
            p.push(i);
            
            if(l === 0)
                l = p.length -1;
            else
                l -= 1;            
        }
    }
    
    return ans;
}
