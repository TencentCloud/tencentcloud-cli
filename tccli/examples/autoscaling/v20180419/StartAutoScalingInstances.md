**Example 1: Starting up CVM instances**



Input: 

```
tccli as StartAutoScalingInstances --cli-unfold-argument  \
    --AutoScalingGroupId asg-boz1qhnk\
    --InstanceIds ins-cri8d02t ins-osckfnm7
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

