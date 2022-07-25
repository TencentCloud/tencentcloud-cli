**Example 1: 按关机不收费模式关闭伸缩组内实例**



Input: 

```
tccli as StopAutoScalingInstances --cli-unfold-argument  \
    --AutoScalingGroupId asg-boz1qhnk \
    --StoppedMode STOP_CHARGING \
    --InstanceIds ins-osckfnm7 ins-cri8d02t
```

Output: 
```
{
    "Response": {
        "ActivityId": "asa-m1ebiskl",
        "RequestId": "f3e2873c-af7c-43ee-8aa7-53565d4181c2"
    }
}
```

