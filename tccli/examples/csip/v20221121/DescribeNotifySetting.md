**Example 1: 示例1**



Input: 

```
tccli csip DescribeNotifySetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AssetRange": 1,
                "BeginTime": "00:00:00",
                "EndTime": "23:59:59",
                "Mode": 0,
                "Module": "Alert",
                "Option": [
                    "CRITICAL"
                ],
                "Status": 1
            }
        ],
        "MemberId": [
            "mem-tencent-ae85b7873563d4bc"
        ],
        "RequestId": "ee85ee67-aa09-4eb0-9d73-ebb63b46bc90"
    }
}
```

