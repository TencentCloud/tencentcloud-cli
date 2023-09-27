**Example 1: 伸缩组内实例退出备用中状态**

伸缩组 asg-boz1qhnk 中实例 ins-osckfnm7, ins-cri8d02t 退出备用中状态

Input: 

```
tccli as ExitStandby --cli-unfold-argument  \
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

