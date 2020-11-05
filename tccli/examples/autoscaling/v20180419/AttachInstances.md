**Example 1: Adding an instance to a scaling group**



Input: 

```
tccli as AttachInstances --cli-unfold-argument  \
    --AutoScalingGroupId asg-boz1qhnk\
    --InstanceIds ins-cri8d02t ins-osckfnm7
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

