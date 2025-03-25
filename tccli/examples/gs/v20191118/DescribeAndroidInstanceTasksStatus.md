**Example 1: 查询安卓实例任务状态**

查询安卓实例任务状态

Input: 

```
tccli gs DescribeAndroidInstanceTasksStatus --cli-unfold-argument  \
    --TaskIds 615cf0a4-075e-4cf5-b26f-d786363daccd
```

Output: 
```
{
    "Response": {
        "TaskStatusSet": [
            {
                "TaskId": "615cf0a4-075e-4cf5-b26f-d786363daccd",
                "Status": "SUCCESS",
                "AndroidInstanceId": "cai-abcd1234"
            }
        ],
        "RequestId": "e54a0e39-4d84-41ab-953f-2f2a72d92546"
    }
}
```

