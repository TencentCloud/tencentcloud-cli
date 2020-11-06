**Example 1: 获取任务状态**

获取任务状态

Input: 

```
tccli ds DescribeTaskStatus --cli-unfold-argument  \
    --Module CommonMng \
    --Operation DescribeTaskStatus \
    --TaskId 255
```

Output: 
```
{
    "Response": {
        "RequestId": "13c00ef1-f3cb-4b1e-be8d-11a01b0d13fd",
        "TaskResult": "{\"ContractResId\": \"dcc-480rzey2ge\"}",
        "TaskType": "010"
    }
}
```

