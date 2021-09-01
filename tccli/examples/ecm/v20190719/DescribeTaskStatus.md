**Example 1: 获取创建镜像任务状态**



Input: 

```
tccli ecm DescribeTaskStatus --cli-unfold-argument  \
    --TaskSet.0.Operation CreateImage \
    --TaskSet.0.TaskId 1528600
```

Output: 
```
{
    "Response": {
        "RequestId": "6660b3b4-c51f-11ea-a187-52540002f896",
        "TaskSet": [
            {
                "TaskId": 1528600,
                "Message": "Create image failed",
                "Status": "FAILED",
                "EndTime": "2020-07-13 00:37:51",
                "AddTime": "2020-07-13 00:37:19",
                "Operation": "CreateImage"
            }
        ]
    }
}
```

