**Example 1: 从伸缩组创建节点池**



Input: 

```
tccli tke CreateClusterNodePoolFromExistingAsg --cli-unfold-argument  \
    --ClusterId cls-xxxxxx \
    --AutoscalingGroupId asg-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "NodePoolId": "np-xxxxxxxx",
        "RequestId": "xxxxxxxx"
    }
}
```

