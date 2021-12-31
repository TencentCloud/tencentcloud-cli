**Example 1: 共享型实例升级为性能容量型**



Input: 

```
tccli clb ModifyLoadBalancerSla --cli-unfold-argument  \
    --LoadBalancerSla.0.LoadBalancerId lb-db2n**** \
    --LoadBalancerSla.0.SlaType SLA
```

Output: 
```
{
    "Response": {
        "RequestId": "c1157c81-f3dc-4f2a-9346-76f161d548eb"
    }
}
```

