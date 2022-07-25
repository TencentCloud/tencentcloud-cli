**Example 1: 将传统负载均衡器lb-crhgatrf从伸缩组中移出**



Input: 

```
tccli as DetachLoadBalancers --cli-unfold-argument  \
    --AutoScalingGroupId asg-12wjuh0s \
    --LoadBalancerIds lb-crhgatrf
```

Output: 
```
{
    "Response": {
        "ActivityId": "asa-67izy66g",
        "RequestId": "bd3c91e8-3051-4c02-ac58-54d47b9c9d63"
    }
}
```

**Example 2: 将应用型负载均衡器lb-23aejgcv（监听器为lbl-ncw704sn，转发路径为loc-l3hmaev9）从伸缩组中移出**



Input: 

```
tccli as DetachLoadBalancers --cli-unfold-argument  \
    --AutoScalingGroupId asg-12wjuh0s \
    --ForwardLoadBalancerIdentifications.0.LocationId loc-l3hmaev9 \
    --ForwardLoadBalancerIdentifications.0.ListenerId lbl-ncw704sn \
    --ForwardLoadBalancerIdentifications.0.LoadBalancerId lb-23aejgcv
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

