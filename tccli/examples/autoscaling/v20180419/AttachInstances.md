**Example 1: 添加实例到伸缩组中**



Input: 

```
tccli as AttachInstances --cli-unfold-argument  \
    --AutoScalingGroupId asg-boz1qhnk \
    --InstanceIds ins-osckfnm7 ins-cri8d02t
```

Output: 
```
{
    "Response": {
        "ActivityId": "asa-q59zikez",
        "RequestId": "5b039ee6-e8ff-4605-bb24-b45337747431"
    }
}
```

