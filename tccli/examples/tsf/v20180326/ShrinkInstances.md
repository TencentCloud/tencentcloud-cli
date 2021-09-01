**Example 1: 虚拟机部署组下线实例**

虚拟机部署组下线实例

Input: 

```
tccli tsf ShrinkInstances --cli-unfold-argument  \
    --GroupId group-xxxxxxx \
    --InstanceIdList ins-xxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "0833008a-119d-4158-a4b6-94d0f4d0f07d",
        "Result": {
            "TaskId": "task-xxxxxxx"
        }
    }
}
```

