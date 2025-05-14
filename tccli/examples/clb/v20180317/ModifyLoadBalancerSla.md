**Example 1: 实例规格调整**

将按量计费模式的共享型实例升级为性能容量型实例，或性能容量型实例的规格调整，按需设置SlaType即为最终实例的规格。

Input: 

```
tccli clb ModifyLoadBalancerSla --cli-unfold-argument  \
    --LoadBalancerSla.0.SlaType clb.c3.medium \
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

