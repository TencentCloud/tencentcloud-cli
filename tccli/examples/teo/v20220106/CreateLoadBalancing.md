**Example 1: 创建负载均衡**



Input: 

```
tccli teo CreateLoadBalancing --cli-unfold-argument  \
    --OriginId origin-xxx origin-yyy \
    --ZoneId zone-xxx \
    --Host test.123.com \
    --Type dns_only \
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

