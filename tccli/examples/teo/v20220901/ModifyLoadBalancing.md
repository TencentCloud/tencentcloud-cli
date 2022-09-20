**Example 1: 修改负载均衡**



Input: 

```
tccli teo ModifyLoadBalancing --cli-unfold-argument  \
    --ZoneId zone-27q0p0bali16 \
    --LoadBalancingId lb-97c8396e-cb88-4c9c-98d9-38e86463d12e \
    --Type dns_only \
    --OriginGroupId orgin-2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a \
    --BackupOriginGroupId  \
    --TTL 600
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-ac39-1706cbf8a707"
    }
}
```

