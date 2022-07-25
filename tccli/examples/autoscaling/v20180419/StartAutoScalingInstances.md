**Example 1: 开启 CVM 实例**



Input: 

```
tccli as StartAutoScalingInstances --cli-unfold-argument  \
    --AutoScalingGroupId asg-boz1qhnk \
    --InstanceIds ins-osckfnm7 ins-cri8d02t
```

Output: 
```
{
    "Response": {
        "ActivityId": "asa-a023dwdj",
        "RequestId": "28cf9089-2b76-4934-9d1b-b2694c679ff0"
    }
}
```

