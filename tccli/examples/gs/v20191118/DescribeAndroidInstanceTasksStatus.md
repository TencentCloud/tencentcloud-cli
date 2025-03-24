**Example 1: 查询安卓实例任务状态**

查询安卓实例任务状态

Input: 

```
tccli gs DescribeAndroidInstanceTasksStatus --cli-unfold-argument  \
    --TaskIds 123
```

Output: 
```
{
    "Response": {
        "TaskStatusSet": [
            {
                "TaskId": "123",
                "Status": "SUCCESS",
                "AndroidInstanceId": "id-test"
            }
        ],
        "RequestId": "e54a0e39-4d84-41ab-953f-2f2a72d92546"
    }
}
```

