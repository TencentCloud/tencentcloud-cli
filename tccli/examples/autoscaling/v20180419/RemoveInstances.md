**Example 1: Removing instances from a scaling group**



Input: 

```
tccli as RemoveInstances --cli-unfold-argument  \
    --AutoScalingGroupId asg-boz1qhnk\
    --InstanceIds ins-cri8d02t ins-osckfnm7
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

