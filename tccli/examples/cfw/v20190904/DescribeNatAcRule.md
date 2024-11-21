**Example 1: 查询NAT访问控制列表实例1**

查询NAT访问控制出向规则列表，其中Filters中 Direction 为0时表示查询出向规则列表，为1时表示查询入向规则列表

Input: 

```
tccli cfw DescribeNatAcRule --cli-unfold-argument  \
    --Filters.0.Name Direction \
    --Filters.0.Values 0 \
    --Filters.0.OperatorType 1 \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Data": [
            {
                "Uuid": 238778,
                "InternalUuid": 1726341068438565,
                "OrderIndex": 19,
                "SourceContent": "ins-gt3h3i8f",
                "SourceType": "instance",
                "TargetContent": "mb_1300448058_1702866694255",
                "TargetType": "template",
                "Port": "-1/-1",
                "Protocol": "ANY",
                "Scope": "ap-guangzhou",
                "ScopeDesc": "广州地域",
                "Direction": 0,
                "RuleAction": "log",
                "Description": "autotest_nat_add",
                "Count": 0,
                "LastHitTime": "2024-11-03 03:14:44",
                "Enable": "true",
                "Invalid": 0,
                "CountryCode": 0,
                "CityCode": 0,
                "CountryName": "中国",
                "CityName": "广东省",
                "IsRegion": 0,
                "CloudCode": "0",
                "IsCloud": 0,
                "InstanceName": "proIns",
                "Status": 0,
                "BetaList": [],
                "ParamTemplateId": "pp-336ad325",
                "ParamTemplateName": "andy",
                "TargetName": "prodst",
                "SourceName": "prosrc"
            }
        ],
        "AllTotal": 1,
        "RequestId": "efa6461b-9410-4cd8-9168-73f37d6ed532"
    }
}
```

