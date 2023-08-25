**Example 1: 获取COS分类分级任务列表**



Input: 

```
tccli dsgc DescribeDSPACOSDiscoveryTasks --cli-unfold-argument  \
    --DspaId dspa-01 \
    --Limit 0 \
    --TaskId 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Enable": 0,
                "Name": "xx",
                "GeneralRuleSetEnable": 0,
                "Period": 0,
                "TimingStartTime": "20201-08-20 09:20:20",
                "Result": {
                    "Status": 0,
                    "EndTime": "2021-08-20 09:30:00",
                    "Id": 0,
                    "Result": "123"
                },
                "Plan": 0,
                "Description": "test_result"
            }
        ],
        "RequestId": "request_1",
        "TotalCount": 1
    }
}
```

