**Example 1: 示例1 查询企业安全组信息**

查询企业安全组信息

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
                "AclTags": "名称",
                "BetaList": [
                    {
                        "TaskId": "9001",
                        "TaskName": "autotest",
                        "LastTime": "1999-01-01 00:00:01"
                    }
                ],
                "Cidr": "192.16.1.0/24",
                "Detail": "企业安全组描述",
                "InstanceName": "企业安全组实例",
                "IsDelay": 0,
                "IsNew": 1,
                "OrderIndex": 1,
                "ParameterName": "参数模版",
                "Port": "-1/-1",
                "PrivateIp": "1.1.1.1",
                "Protocol": "ANY",
                "ProtocolPortName": "模版",
                "PublicIp": "1.1.1.1",
                "Region": "AllRegion",
                "RuleUuid": 61257,
                "ServiceTemplateId": "ip-didd011",
                "SouCidr": "192.168.1.0/24",
                "SouInstanceName": "模版名称",
                "SouParameterName": "模版名称",
                "SouPrivateIp": "1.1.1.1",
                "SouPublicIp": "1.1.1.1",
                "SourceId": "ipmg-17hphuxg",
                "SourceType": 7,
                "Status": 1,
                "Strategy": 1,
                "TargetId": "cfwrg-b803523898534bcbd9b7d2c7d92c175e1712804418",
                "TargetType": 100,
                "Uuid": "cfw_newsg_1300448058_0.0.0.0/0_17228848067531",
                "Id": 61257
            }
        ],
        "Enable": 2,
        "RequestId": "d835bbe0-99e8-4cb7-a29a-3dfe2eff7d14",
        "Total": 28
    }
}
```

