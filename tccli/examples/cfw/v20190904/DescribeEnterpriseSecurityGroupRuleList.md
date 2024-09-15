**Example 1: 示例1**

示例1

Input: 

```
tccli cfw DescribeEnterpriseSecurityGroupRuleList --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0 \
    --SearchFilters.0.Name common \
    --SearchFilters.0.Values 模板 \
    --SearchFilters.0.OperatorType 9
```

Output: 
```
{
    "Response": {
        "AllTotal": 30,
        "Data": [
            {
                "AclTags": "云防火墙封禁IP自动下发，请勿删除或修改",
                "BetaList": [],
                "Cidr": "",
                "Detail": "云防火墙封禁IP自动下发，请勿删除或修改",
                "InstanceName": "",
                "IsDelay": 0,
                "IsNew": 1,
                "OrderIndex": 1,
                "ParameterName": "",
                "Port": "-1/-1",
                "PrivateIp": "",
                "Protocol": "ANY",
                "ProtocolPortName": "",
                "PublicIp": "",
                "Region": "AllRegion",
                "RuleUuid": 61257,
                "ServiceTemplateId": "",
                "SouCidr": "",
                "SouInstanceName": "",
                "SouParameterName": "云防火墙拦截列表IP地址组IN，请勿删除",
                "SouPrivateIp": "",
                "SouPublicIp": "",
                "SourceId": "ipmg-17hphuxg",
                "SourceType": 7,
                "Status": 1,
                "Strategy": 1,
                "TargetId": "cfwrg-b803523898534bcbd9b7d2c7d92c175e1712804418",
                "TargetType": 100,
                "Uuid": "cfw_newsg_1300448058_0.0.0.0/0_17228848067531"
            }
        ],
        "Enable": 2,
        "RequestId": "d835bbe0-99e8-4cb7-a29a-3dfe2eff7d14",
        "Total": 28
    }
}
```

