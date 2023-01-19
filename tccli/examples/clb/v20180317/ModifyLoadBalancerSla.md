**Example 1: 共享型实例升级为性能容量型**

将按量计费模式的共享型实例升级为性能容量型实例。

Input: 

```
tccli clb ModifyLoadBalancerSla --cli-unfold-argument  \
    --LoadBalancerSla.0.SlaType SLA \
    --LoadBalancerSla.0.LoadBalancerId lb-db2n****
```

Output: 
```
{
    "Response": {
        "RequestId": "c1157c81-f3dc-4f2a-9346-76f161d548eb"
    }
}
```

