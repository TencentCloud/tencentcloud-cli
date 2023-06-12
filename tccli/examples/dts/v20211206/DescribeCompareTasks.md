**Example 1: 查询一致性校验任务列表**

查询一致性校验任务列表

Input: 

```
tccli dts DescribeCompareTasks --cli-unfold-argument  \
    --JobId dts-e7ukka6g
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CheckProcess": {
                    "Message": "",
                    "Status": "",
                    "StepAll": 0,
                    "StepNow": 0,
                    "Percent": 0,
                    "Steps": []
                },
                "CompareProcess": {
                    "Message": "done",
                    "Status": "",
                    "StepAll": 0,
                    "StepNow": 0,
                    "Steps": []
                },
                "CompareTaskId": "dts-amm1jw5q-cmp-bmuum7jk",
                "Conclusion": "same",
                "Config": {
                    "ObjectItems": [
                        {
                            "DbMode": "partial",
                            "DbName": "big100",
                            "SchemaName": "",
                            "TableMode": "partial",
                            "Tables": null,
                            "ViewMode": "none",
                            "Views": null
                        },
                        {
                            "DbMode": "all",
                            "DbName": "db1",
                            "SchemaName": "",
                            "TableMode": "all",
                            "Tables": null,
                            "ViewMode": "all",
                            "Views": null
                        }
                    ],
                    "ObjectMode": "partial"
                },
                "CreatedAt": "2022-07-11 17:21:02",
                "FinishedAt": "2022-07-11 17:24:54",
                "Method": "dataCheck",
                "Options": {
                    "Method": "dataCheck",
                    "SampleRate": 100,
                    "ThreadCount": 1
                },
                "JobId": "dts-amm1jw5q",
                "Message": "done",
                "StartedAt": "2022-07-11 17:24:09",
                "Status": "success",
                "TaskName": "defaultCmpTask"
            }
        ],
        "RequestId": "11d35c90-01bb-11ed-bad9-7b3bbe11abda",
        "TotalCount": 1
    }
}
```

