**Example 1: 获取项目任务列表**



Input: 

```
tccli cme DescribeTasks --cli-unfold-argument  \
    --Platform test
```

Output: 
```
{
    "Response": {
        "RequestId": "efde1a47-f1c9-4c1b-911c-9865a6a4d1ac",
        "TaskBaseInfoSet": [
            {
                "CreateTime": "2020-04-30T03:26:37Z",
                "ErrCode": 0,
                "ErrMsg": "SUCCESS",
                "Progress": 100,
                "Status": "SUCCESS",
                "TaskId": "140-procedurev2-b718fcee09a72470bf665cf55351d810t0",
                "TaskType": "PROJECT_EXPORT"
            }
        ],
        "TotalCount": 1
    }
}
```

