**Example 1: 查询NAT访问控制列表**

查询NAT访问控制列表

Input: 

```
tccli cfw DescribeNatAcRule --cli-unfold-argument  \
    --Index xx \
    --Filters.0.Name xx \
    --Filters.0.Values xx \
    --Filters.0.OperatorType 0 \
    --Limit 1 \
    --Offset 1 \
    --StartTime xx \
    --EndTime xx \
    --Order xx \
    --By xx
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Data": [
            {
                "SourceContent": "xx",
                "TargetContent": "xx",
                "Protocol": "xx",
                "Port": "xx",
                "RuleAction": "xx",
                "Description": "xx",
                "Count": 1,
                "OrderIndex": 1,
                "SourceType": "xx",
                "TargetType": "xx",
                "Uuid": 1,
                "Invalid": 1,
                "IsRegion": 1,
                "CountryCode": 1,
                "CityCode": 1,
                "CountryName": "xx",
                "CityName": "xx",
                "CloudCode": "xx",
                "IsCloud": 1,
                "Enable": "xx",
                "Direction": 1,
                "InstanceName": "xx",
                "InternalUuid": 0,
                "Status": 1
            }
        ],
        "AllTotal": 1,
        "RequestId": "xx"
    }
}
```

