**Example 1: 修改应用型负载均衡器lb-23aejgcv（监听器为lbl-ncw704sn，转发路径为loc-l3hmaev9）的目标规则属性，将端口修改为8080，权重修改为20。**



Input: 

```
tccli as ModifyLoadBalancerTargetAttributes --cli-unfold-argument  \
    --AutoScalingGroupId asg-12wjuh0s \
    --ForwardLoadBalancers.0.TargetAttributes.0.Port 8080 \
    --ForwardLoadBalancers.0.TargetAttributes.0.Weight 20 \
    --ForwardLoadBalancers.0.Region ap-guangzhou \
    --ForwardLoadBalancers.0.LocationId loc-l3hmaev9 \
    --ForwardLoadBalancers.0.ListenerId lbl-ncw704sn \
    --ForwardLoadBalancers.0.LoadBalancerId lb-23aejgcv
```

Output: 
```
{
    "Response": {
        "ActivityId": "asa-9asddelc",
        "RequestId": "8d78668d-61eb-456d-855b-f34f91371089"
    }
}
```

