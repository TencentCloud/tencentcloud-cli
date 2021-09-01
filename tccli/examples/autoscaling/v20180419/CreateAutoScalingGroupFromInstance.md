**Example 1: 根据实例创建启动配置及伸缩组**



Input: 

```
tccli as CreateAutoScalingGroupFromInstance --cli-unfold-argument  \
    --DesiredCapacity 0 \
    --InstanceId ins-19a14o9y \
    --AutoScalingGroupName as-test \
    --MinSize 0 \
    --MaxSize 1 \
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

