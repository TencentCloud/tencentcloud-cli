**Example 1: 调用失败示例**



Input: 

```
tccli bda GetPersonList --cli-unfold-argument  \
    --GroupId testG10 \
    --Offset 0 \
    --Limit 1001
```

Output: 
```
{
    "Response": {
        "RequestId": "c803e3eb-25b4-48d9-b4df-b74c570d110b"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli bda GetPersonList --cli-unfold-argument  \
    --GroupId testG10 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "PersonNum": 1,
        "BodyModelVersion": "1.0",
        "PersonInfos": [
            {
                "PersonName": "testG10P1",
                "PersonId": "testG10P1",
                "TraceInfos": [
                    {
                        "TraceId": "3524775577730961229",
                        "BodyIds": [
                            "3524775577730961229-0"
                        ]
                    }
                ]
            }
        ],
        "RequestId": "2e1841c2-81ee-42db-98ac-6c056aafe9b3"
    }
}
```

