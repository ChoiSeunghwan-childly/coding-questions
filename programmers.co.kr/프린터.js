function solution(p, l) {
    let ans = 0;
    let max = Math.max.apply(null, p)
    while(p.length){
        let i = p.shift();
        
        if (i === max){
            ans += 1;            
            if (l === 0)
                break;
            else 
                l -= 1;    
            max = Math.max.apply(null, p);
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
