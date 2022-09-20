**Example 1: 启用负载均衡**



Input: 

```
tccli teo ModifyLoadBalancingStatus --cli-unfold-argument  \
    --ZoneId zone-27q0p0bali16 \
    --LoadBalancingId lb-97c8396e-cb88-4c9c-98d9-38e86463d12e \
    --Status online
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

**Example 2: 停用负载均衡**



Input: 

```
tccli teo ModifyLoadBalancingStatus --cli-unfold-argument  \
    --ZoneId zone-27q0p0bali16 \
    --LoadBalancingId lb-97c8396e-cb88-4c9c-98d9-38e86463d12e \
    --Status offline
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

