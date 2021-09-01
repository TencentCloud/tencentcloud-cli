**Example 1: 缩容虚拟机部署组**



Input: 

```
tccli tsf ShrinkGroup --cli-unfold-argument  \
    --GroupId group-xxxxxxx
```

Output: 
```
{
    "data": {
        "Response": {
            "RequestId": "6ae4fc90-8153-4b71-8310-a8ca5ad85440",
            "Result": {
                "TaskId": "task-xxxxxxx"
            }
        }
    },
    "code": 0
}
```

