**Example 1: 查询互联网边界访问控制列表**

查询互联网边界访问控制列表

Input: 

```
tccli cfw DescribeAclRule --cli-unfold-argument  \
    --Index abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.OperatorType 0 \
    --Limit 1 \
    --Offset 1 \
    --StartTime abc \
    --EndTime abc \
    --Order abc \
    --By abc
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Data": [
            {
                "SourceContent": "abc",
                "TargetContent": "abc",
                "Protocol": "abc",
                "Port": "abc",
                "RuleAction": "abc",
                "Description": "abc",
                "Count": 1,
                "OrderIndex": 1,
                "SourceType": "abc",
                "TargetType": "abc",
                "Uuid": 1,
                "Invalid": 1,
                "IsRegion": 1,
                "CountryCode": 1,
                "CityCode": 1,
                "CountryName": "abc",
                "CityName": "abc",
                "CloudCode": "abc",
                "IsCloud": 1,
                "Enable": "abc",
                "Direction": 1,
                "InstanceName": "abc",
                "InternalUuid": 0,
                "Status": 1,
                "BetaList": [
                    {
                        "TaskId": 0,
                        "TaskName": "abc",
                        "LastTime": "abc"
                    }
                ],
                "Scope": "abc",
                "InternetBorderUuid": "abc"
            }
        ],
        "AllTotal": 1,
        "RequestId": "abc"
    }
}
```

