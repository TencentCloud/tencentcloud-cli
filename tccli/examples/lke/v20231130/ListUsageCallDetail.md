**Example 1: 列表查询单次调用明细**

列表查询单次调用明细

Input: 

```
tccli lke ListUsageCallDetail --cli-unfold-argument  \
    --CallType AllCallType \
    --ModelName cs-normal-70b \
    --StartTime 1723564800 \
    --EndTime 1726156799 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppName": "",
                "CallTime": "1724946200",
                "CallType": "对话调用",
                "Id": "e8h_20240701_194330_474_XRMUA92T",
                "InputTokenUsage": 471,
                "ModelName": "精调知识大模型高级版",
                "OutputTokenUsage": 886,
                "SearchUsage": 0,
                "TotalTokenUsage": 1357,
                "UinAccount": "600000562455"
            }
        ],
        "RequestId": "9332ab9b-dec8-481e-87a8-af6983ac9fe7",
        "Total": 1
    }
}
```

