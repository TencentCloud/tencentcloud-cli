**Example 1: 查询刷新预热任务状态**



Input: 

```
tccli hcdn DescribeCacheTask --cli-unfold-argument  \
    --StartTime 2022-09-29 17:17:38 \
    --EndTime 2022-09-29 17:37:38
```

Output: 
```
{
    "Response": {
        "RequestId": "edd43e1f-e192-4541-a07d-e4c0da17d9c6",
        "TotalCount": 4,
        "TaskResult": [
            {
                "FileUrl": "https://www.xxx1.com/xxx1.flv",
                "Status": 3,
                "TaskId": "83c3688b-0c01-4d4b-8f45-64d2c71e21f7",
                "CreateTime": "2022-10-09 10:53:45",
                "TaskType": 2
            },
            {
                "FileUrl": "https://www.xxx2.com/xxx2.flv",
                "Status": 3,
                "TaskId": "83c3688b-0c01-4d4b-8f45-64d2c71e21f7",
                "CreateTime": "2022-10-09 10:53:45",
                "TaskType": 2
            },
            {
                "FileUrl": "https://www.xxx3.com/xxx3.flv",
                "Status": 3,
                "TaskId": "20830af4-3d4d-46f3-b06b-88f15028aaec",
                "CreateTime": "2022-10-09 10:54:08",
                "TaskType": 2
            },
            {
                "FileUrl": "https://www.xxx4.com/xxx4.flv",
                "Status": 3,
                "TaskId": "20830af4-3d4d-46f3-b06b-88f15028aaec",
                "CreateTime": "2022-10-09 10:54:08",
                "TaskType": 2
            }
        ]
    }
}
```

