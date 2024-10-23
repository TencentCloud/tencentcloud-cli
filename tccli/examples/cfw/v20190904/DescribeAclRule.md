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
                        "LastTime": "",
                        "TaskId": 9070,
                        "TaskName": "aa"
                    }
                ],
                "CityCode": 0,
                "CityName": "",
                "CloudCode": "",
                "Count": 0,
                "CountryCode": 0,
                "CountryName": "",
                "Description": "测试命中",
                "Direction": 0,
                "Enable": "false",
                "InstanceName": "",
                "InternalUuid": 0,
                "InternetBorderUuid": "1300448058_0.0.0.0/0_1729685657863970",
                "Invalid": 0,
                "IsCloud": 0,
                "IsRegion": 0,
                "LastHitTime": "",
                "OrderIndex": 2,
                "ParamTemplateId": "",
                "ParamTemplateName": "",
                "Port": "-1/-1",
                "Protocol": "HTTPS",
                "RuleAction": "log",
                "Scope": "serial",
                "SourceContent": "0.0.0.0/0",
                "SourceName": "",
                "SourceType": "net",
                "Status": 0,
                "TargetContent": "www.qq.com",
                "TargetName": "",
                "TargetType": "domain",
                "Uuid": 148183
            }
        ],
        "RequestId": "985187d2-9a80-4ee7-b519-ad48e75f6588",
        "Total": 6
    }
}
```

