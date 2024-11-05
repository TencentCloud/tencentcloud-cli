**Example 1: 获取Api请求详情信息**

获取Api请求详情信息

Input: 

```
tccli waf DescribeApiDetail --cli-unfold-argument  \
    --Domain hzh.qcloud.com \
    --Method POST \
    --ApiName /test
```

Output: 
```
{
    "Response": {
        "RequestId": "6088f081-3e69-421e-9bbe-b91510af0414",
        "Log": "{\"other\":{}}",
        "ParameterList": [],
        "Scene": "waf",
        "SensitiveFields": [],
        "IsActive": false,
        "IpCount": 0,
        "RegionCount": 0,
        "EventCount": 0,
        "SensitiveCount": 0,
        "RspLog": "{\"other\":{}}",
        "Level": 0
    }
}
```

