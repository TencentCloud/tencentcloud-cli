**Example 1: 查询规则组中规则列表接口**



Input: 

```
tccli fwm DescribeSecurityGroupRules --cli-unfold-argument  \
    --GroupId fwmrg-i3pvf19a \
    --Filters.0.Name RuleId \
    --Filters.0.Values 6eaf61e \
    --Filters.0.OperatorType 9
```

Output: 
```
{
    "Response": {
        "AllTotalCount": 7,
        "RequestId": "d1f4711c-a542-4b7f-9443-7fd31437edd4",
        "Rules": [
            {
                "BelongMember": {
                    "AppId": "1300448058",
                    "MemberId": "mem-tencent-e4f32cfd87465a17",
                    "Nickname": "天空之蓝",
                    "Uin": "100011616646"
                },
                "Cidr": "",
                "Detail": "1",
                "DnsParseCount": {
                    "InvalidCount": 0,
                    "ValidCount": 0
                },
                "Id": 7884,
                "InstanceName": "",
                "IpVersion": "ipv4",
                "OrderIndex": 7,
                "ParameterName": "",
                "Port": "-1/-1",
                "PrivateIp": "",
                "Protocol": "ANY",
                "ProtocolPortName": "",
                "PublicIp": "",
                "Region": "",
                "RuleId": "6eaf61e3-2f5f-435c-b3d1-c39dae46a7de",
                "Scope": "SG",
                "ServiceTemplateId": "",
                "SouCidr": "",
                "SouInstanceName": "",
                "SouParameterName": "",
                "SouPrivateIp": "",
                "SouPublicIp": "",
                "SourceId": "0.0.0.0/0",
                "SourceType": 0,
                "Strategy": 2,
                "TargetId": "0.0.0.0/0",
                "TargetType": 0
            }
        ],
        "TotalCount": 1
    }
}
```

