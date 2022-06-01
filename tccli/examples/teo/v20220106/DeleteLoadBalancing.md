**Example 1: 删除负载均衡**



Input: 

```
tccli teo DeleteLoadBalancing --cli-unfold-argument  \
    --ZoneId zone-xxx \
    --LoadBalancingId lb-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "LoadBalancingId": "lb-xxx"
    }
}
```

