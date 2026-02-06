**Example 1: 列表查询单次调用明细示例**

列表查询单次调用明细示例

Input: 

```
tccli lke ListUsageCallDetail --cli-unfold-argument  \
    --ModelName cs-normal-70b \
    --StartTime 1758988800 \
    --EndTime 1759075199 \
    --CallType AllCallType \
    --PageNumber 1 \
    --PageSize 10 \
    --AppType knowledge_qa \
    --SpaceId default_space \
    --StatStartTime 1758988800 \
    --StatEndTime 1759075199
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppName": "jacobs-0926",
                "BillingTag": "null",
                "CallTime": "1759057890",
                "CallType": "对话调用-分享用户端对话",
                "Id": "Bd4_20250928_191127_831_tlwHTOyB",
                "InputTokenUsage": 168,
                "ModelName": "youtu-mrc-pro",
                "OutputTokenUsage": 15,
                "PageUsage": 183,
                "SearchUsage": 0,
                "SubScene": "",
                "TotalTokenUsage": 183,
                "UinAccount": "700000963993"
            },
            {
                "AppName": "jacobs-0926",
                "BillingTag": "null",
                "CallTime": "1759057441",
                "CallType": "对话调用-分享用户端对话",
                "Id": "M2B_20250928_190357_441_Uyk4R1tn",
                "InputTokenUsage": 145,
                "ModelName": "youtu-mrc-pro",
                "OutputTokenUsage": 15,
                "PageUsage": 160,
                "SearchUsage": 0,
                "SubScene": "",
                "TotalTokenUsage": 160,
                "UinAccount": "700000963993"
            }
        ],
        "RequestId": "e8d2fc9c-0cbd-4ca6-87cf-01fa5d8bd6bf",
        "Total": 2
    }
}
```

