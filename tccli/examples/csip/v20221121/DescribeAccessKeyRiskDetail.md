**Example 1: 查询AccessKey风险详情**



Input: 

```
tccli csip DescribeAccessKeyRiskDetail --cli-unfold-argument  \
    --ID 7
```

Output: 
```
{
    "Response": {
        "AlarmCount": 0,
        "CamCount": 3,
        "RequestId": "9e9119de-b50e-4011-830d-7d0e698e29b7",
        "RiskInfo": {
            "AccessKey": "AKID******",
            "AccessKeyID": 10066,
            "AccessKeyRemark": "",
            "AppID": 100001,
            "CheckStatus": 0,
            "Description": "应该对私有网络(VPC)的操作权限进行收敛，不应拥有如下敏感接口权限：CreateCcnRouteTables, CreateNatGatewayDestinationIpPortTranslationNatRule, CreateNatGatewaySourceIpTranslationNatRule, CreateSecurityGroup, CreateSecurityGroupWithPolicies, CreateVpcEndPoint, CreateVpcPeeringConnection",
            "Evidence": "vpc:*",
            "ID": 7,
            "Level": 4,
            "Name": "应该对私有网络(VPC)的操作权限进行收敛",
            "Nickname": "name",
            "RiskRuleID": 28,
            "RiskTime": "2025-03-13 14:00:43",
            "RiskType": 0,
            "Status": 0,
            "SubNickname": "name",
            "SubUin": "1000001",
            "Tag": [],
            "Type": 1,
            "Uin": "100001"
        }
    }
}
```

