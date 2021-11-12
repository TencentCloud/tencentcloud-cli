**Example 1: 提升性能保障规格**



Input: 

```
tccli clb ModifyLoadBalancerSla --cli-unfold-argument  \
    --LoadBalancerSla.0.LoadBalancerId lb-db2nt5l2 \
    --LoadBalancerSla.0.SlaType sla-3
```

Output: 
```
{
    "Response": {
        "RequestId": "c1157c81-f3dc-4f2a-9346-76f161d548eb"
    }
}
```

