**Example 1: 查询互联网边界访问控制列表示例**

查询互联网边界出向访问控制列表，其中Filters中Direction 为0表示查询出向访问控制规则列表，为1时表示查询入向访问控制列表

Input: 

```
tccli cfw DescribeAclRule --cli-unfold-argument  \
    --Filters.0.Name Direction \
    --Filters.0.Values 0 \
    --Filters.0.OperatorType 1 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "AllTotal": 6,
        "Data": [
            {
                "BetaList": [
                    {
                        "LastTime": "2024-11-03 03:16:44",
                        "TaskId": 9070,
                        "TaskName": "dayCron"
                    }
                ],
                "CityCode": 0,
                "Count": 0,
                "CountryCode": 0,
                "CountryName": "中国",
                "Description": "测试命中",
                "CityName": "广东省",
                "Direction": 0,
                "Enable": "false",
                "InstanceName": "pro-ins",
                "InternalUuid": 0,
                "InternetBorderUuid": "1300448058_0.0.0.0/0_1729685657863970",
                "Invalid": 0,
                "IsCloud": 0,
                "CloudCode": "0",
                "IsRegion": 0,
                "LastHitTime": "2024-11-03 03:14:44",
                "OrderIndex": 2,
                "ParamTemplateId": "pp-738fd652",
                "ParamTemplateName": "pro参数模版",
                "Port": "-1/-1",
                "Protocol": "HTTPS",
                "RuleAction": "log",
                "Scope": "serial",
                "SourceContent": "0.0.0.0/0",
                "SourceName": "proSrc",
                "SourceType": "net",
                "Status": 0,
                "TargetContent": "www.qq.com",
                "TargetName": "pro",
                "TargetType": "domain",
                "Uuid": 148183
            }
        ],
        "RequestId": "985187d2-9a80-4ee7-b519-ad48e75f6588",
        "Total": 6
    }
}
```

