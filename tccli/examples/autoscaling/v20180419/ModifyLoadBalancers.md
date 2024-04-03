**Example 1: 清空伸缩组的负载均衡器**



Input: 

```
tccli as ModifyLoadBalancers --cli-unfold-argument  \
    --AutoScalingGroupId asg-12wjuh0s
```

Output: 
```
{
    "Response": {
        "ActivityId": "asa-rp63a5q8",
        "RequestId": "7de5a82f-b781-4302-b723-e7a879c20767"
    }
}
```

**Example 2: 将伸缩组的负载均衡器修改为传统负载均衡器lb-crhgatrf**



Input: 

```
tccli as ModifyLoadBalancers --cli-unfold-argument  \
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

**Example 3: 将伸缩组的负载均衡器修改为应用型负载均衡器lb-23aejgcv，监听器为lbl-ncw704sn**



Input: 

```
tccli as ModifyLoadBalancers --cli-unfold-argument  \
    --AutoScalingGroupId asg-12wjuh0s \
    --ForwardLoadBalancers.0.TargetAttributes.0.Port 8080 \
    --ForwardLoadBalancers.0.TargetAttributes.0.Weight 10 \
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

