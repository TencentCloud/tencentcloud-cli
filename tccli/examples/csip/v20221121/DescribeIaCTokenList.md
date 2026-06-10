**Example 1: 示例1**



Input: 

```
tccli csip DescribeIaCTokenList --cli-unfold-argument  \
    --MemberId mem-a6df317cb6a8c424 \
    --Filter.Limit 10 \
    --Filter.Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppId": 260082268,
                "FileCnt": 1004,
                "Id": 10036,
                "LastScanStatus": "SCAN_ERR",
                "LastScanTime": "2026-04-07T08:00:28Z",
                "Name": "zunlong",
                "Period": 60,
                "Token": "73d2721f-1152-4300-a4a4-a206f7ce8841"
            }
        ],
        "TotalCount": 27,
        "RequestId": "8eeceeb1-a62d-4a5f-911d-03be746b2bc3"
    }
}
```

