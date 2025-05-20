**Example 1: cfw实例运行状态查询**



Input: 

```
tccli cfw DescribeCFWEngineStatus --cli-unfold-argument  \
    --UniqInsId ins-h1fxg9l4 \
    --StartTime 2025-04-15 00:00:00 \
    --EndTime 2025-04-15 17:00:00
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Status": "abnormal",
                "Summary": "引擎高负载",
                "Url": ""
            }
        ],
        "RequestId": "39268ae2-7796-47ed-a3b9-d8f8d8eb8dc8"
    }
}
```

