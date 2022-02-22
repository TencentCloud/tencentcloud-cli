**Example 1: 查询 kill 会话任务执行结果**



Input: 

```
tccli dbbrain DescribeProxySessionKillTasks --cli-unfold-argument  \
    --InstanceId xx \
    --Product xx \
    --AsyncRequestIds 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "TotalCount": 1,
        "Tasks": [
            {
                "Progress": 100,
                "InstProxyList": [
                    "6511ec503b047be913e30c1bbf1f2c8c861e8347",
                    "2ce994dadc0e2b27e76ae13d04ab9eadd9665397",
                    "db0fcd29867e65eb999ce99383d7a06cd21ca077"
                ],
                "AsyncRequestId": 7677678,
                "EndTime": "2020-09-22T00:00:00+00:00",
                "InstProxyCount": 3,
                "InstanceId": "crs-o5chheqz",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "StartTime": "2020-09-22T00:00:00+00:00",
                "TaskStatus": "finished",
                "FinishedProxyList": [
                    "6511ec503b047be913e30c1bbf1f2c8c861e8347",
                    "2ce994dadc0e2b27e76ae13d04ab9eadd9665397",
                    "db0fcd29867e65eb999ce99383d7a06cd21ca077"
                ],
                "FailedProxyList": []
            }
        ]
    }
}
```

