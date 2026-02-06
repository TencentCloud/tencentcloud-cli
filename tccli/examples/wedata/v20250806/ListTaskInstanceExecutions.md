**Example 1: 获取任务实例执行列表**



Input: 

```
tccli wedata ListTaskInstanceExecutions --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --InstanceKey 20250714200130106_2025-10-01 00:00:00 \
    --TimeZone UTC+8 \
    --PageSize 1 \
    --PageNumber 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CostTime": 11,
                    "ExecutionPhaseList": [
                        {
                            "DetailState": "EXPIRED",
                            "EndTime": "2025-08-20 17:57:26",
                            "StartTime": "2025-08-20 17:57:26"
                        }
                    ],
                    "InstanceKey": "20250714200130106_2025-10-01 00:00:00",
                    "InstanceState": "EXPIRED",
                    "LifeRoundNum": 0,
                    "RunType": "ADDITION",
                    "Tries": 0
                }
            ],
            "PageNumber": 10,
            "PageSize": 1,
            "TotalCount": 109,
            "TotalPageNumber": 109
        },
        "RequestId": "85d27a71-445c-4c6b-8d0e-c14209a2903b"
    }
}
```

