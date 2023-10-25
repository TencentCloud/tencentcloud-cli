**Example 1: 示例**

创建试用订单

Input: 

```
tccli cwp CreateWhiteListOrder --cli-unfold-argument  \
    --LicenseType 1 \
    --LicenseNum 10 \
    --Deadline 10 \
    --SourceType 1 \
    --RuleName asset_center
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx",
        "Resource": {
            "Id": 1,
            "ResourceId": "white_xxxx",
            "BeginTime": "2022-05-31 00:00:00",
            "EndTime": "2022-06-10 00:00:00",
            "LicenseType": 1
        }
    }
}
```

