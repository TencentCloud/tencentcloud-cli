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
        "RequestId": "d1245804-b922-4c3b-8499-f95dce26b33c",
        "Resource": {
            "Id": 1,
            "ResourceId": "white_2415**",
            "BeginTime": "2022-05-31 00:00:00",
            "EndTime": "2022-06-10 00:00:00",
            "LicenseType": 1
        }
    }
}
```

