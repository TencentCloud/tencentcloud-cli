**Example 1: 虚拟机部署组添加实例**



Input: 

```
tccli tsf ExpandGroup --cli-unfold-argument  \
    --GroupId group-xxxxxxx \
    --InstanceIdList ins-xxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "fa97858f-7b91-4ab3-a701-7a21d69a2493",
        "Result": {
            "TaskId": "task-xxxxxxx"
        }
    }
}
```

