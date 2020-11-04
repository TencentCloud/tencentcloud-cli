**Example 1: 示例**



Input: 

```
tccli npp DescribeCallerDisplayList --cli-unfold-argument  \
    --BizAppId xxx
```

Output: 
```
{
    "Response": {
        "AppId": "65535",
        "CodeList": [
            {
                "Nation": "0086",
                "Phone": "025xxxx"
            },
            {
                "Nation": "0086",
                "Phone": "025xxxxx"
            }
        ],
        "ErrorCode": "0",
        "Msg": "",
        "RequestId": "3f166c9c-595e-47cf-ba43-58b3e8f1dd5b"
    }
}
```

