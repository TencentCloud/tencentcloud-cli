**Example 1: 从伸缩组删除实例**



Input: 

```
tccli as RemoveInstances --cli-unfold-argument  \
    --AutoScalingGroupId asg-boz1qhnk \
    --InstanceIds ins-osckfnm7 ins-cri8d02t
```

Output: 
```
{
    "Response": {
        "ActivityId": "asa-dne04cxp",
        "RequestId": "5b039ee6-e8ff-4605-bb24-b45337747431"
    }
}
```

