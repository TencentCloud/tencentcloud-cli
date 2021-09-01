**Example 1: 停止虚拟机部署组**



Input: 

```
tccli tsf StopGroup --cli-unfold-argument  \
    --GroupId group-xxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "aaa27977-468d-4b1c-a88b-0656691d6840",
        "Result": {
            "TaskId": "task-xxxxxxx"
        }
    }
}
```

