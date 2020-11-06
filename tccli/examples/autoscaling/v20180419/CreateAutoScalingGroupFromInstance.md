**Example 1: Creating launch configuration and scaling group based on an instance**



Input: 

```
tccli as CreateAutoScalingGroupFromInstance --cli-unfold-argument  \
    --AutoScalingGroupName as-test \
    --InstanceId ins-19a14o9y \
    --MinSize 0 \
    --MaxSize 1 \
    --DesiredCapacity 0 \
    --InheritInstanceTag False
```

Output: 
```
{
    "Response": {
        "AutoScalingGroupId": "asg-cqatht5b",
        "RequestId": "19c10733-d0e8-4f58-ac82-e1b1affb0bbb"
    }
}
```

