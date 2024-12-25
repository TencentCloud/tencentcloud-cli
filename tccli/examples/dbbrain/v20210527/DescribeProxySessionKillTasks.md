**Example 1: 查询 kill 会话任务执行结果**



Input: 

```
tccli dbbrain DescribeProxySessionKillTasks --cli-unfold-argument  \
    --InstanceId crs-test1234 \
    --Product redis \
    --AsyncRequestIds 10474110
```

Output: 
```
{
    "Response": {
        "RequestId": "e5c42270-c19c-11ef-b367-d5cedbfa06d8",
        "TotalCount": 1,
        "Tasks": [
            {
                "Progress": 100,
                "InstProxyList": [
                    "6511ec503b047be913e30c1bbf1f2c8c861e8347",
                    "2ce994dadc0e2b27e76ae13d04ab9eadd9665397",
                    "db0fcd29867e65eb999ce99383d7a06cd21ca077"
                ],
                "AsyncRequestId": 10474110,
                "EndTime": "2020-09-22T00:00:00+00:00",
                "InstProxyCount": 3,
                "InstanceId": "crs-test1234",
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

