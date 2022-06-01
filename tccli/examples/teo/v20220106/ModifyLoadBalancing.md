**Example 1: 修改负载均衡**



Input: 

```
tccli teo ModifyLoadBalancing --cli-unfold-argument  \
    --ZoneId zone-xxx \
    --LoadBalancingId lb-xxx \
    --Type dns_only \
    --OriginId origin-xxx origin-yyy \
    --TTL 123
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

