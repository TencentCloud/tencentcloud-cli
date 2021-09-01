**Example 1: 查询设备日志列表**



Input: 

```
tccli iotvideo DescribeLogs --cli-unfold-argument  \
    --Tid 031400005e005a3816c529f9e82efe9b \
    --LogType 1 \
    --StartTime 0 \
    --EndTime 1582077707 \
    --Limit 10 \
    --Offset 0 \
    --DataObject **
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Occurtime": 1577964702,
                "LogType": 1,
                "DataObject": "ProReadonly._online",
                "OldValue": "{\"stVal\":0,\"t\":0}",
                "NewValue": "{\"stVal\":1,\"t\":1577964702}"
            },
            {
                "Occurtime": 1577964763,
                "LogType": 1,
                "DataObject": "ProReadonly._online",
                "OldValue": "{\"stVal\":1,\"t\":1577964702}",
                "NewValue": "{\"stVal\":0,\"t\":1577964762}"
            },
            {
                "Occurtime": 1577964787,
                "LogType": 1,
                "DataObject": "ProReadonly._online",
                "OldValue": "{\"stVal\":0,\"t\":1577964702}",
                "NewValue": "{\"stVal\":1,\"t\":1577964787}"
            },
            {
                "Occurtime": 1577964848,
                "LogType": 1,
                "DataObject": "ProReadonly._online",
                "OldValue": "{\"stVal\":1,\"t\":1577964787}",
                "NewValue": "{\"stVal\":0,\"t\":1577964847}"
            }
        ],
        "TotalCount": 4,
        "RequestId": "0f365132-f8a8-4520-a5c2-7383ad871ecd"
    }
}
```

