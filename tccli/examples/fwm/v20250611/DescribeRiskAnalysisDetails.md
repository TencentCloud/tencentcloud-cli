**Example 1: 获取实时分析风险详情**



Input: 

```
tccli fwm DescribeRiskAnalysisDetails --cli-unfold-argument  \
    --Id 398d5185cb7c4b15e44640a38f78d681 \
    --SearchType analyze
```

Output: 
```
{
    "Response": {
        "EnterpriseSecurityGroupRuleIPV6": [],
        "RequestId": "0831ba3a-9c6d-4b1b-98e2-b92c2499e934"
    }
}
```

**Example 2: 查看指定成员的**



Input: 

```
tccli fwm DescribeRiskAnalysisDetails --cli-unfold-argument  \
    --Id 77c4bea5ce631684079e8d6420d535ed \
    --SearchType analyze \
    --MemberId mem-tencent-e4f32cfd87465a17
```

Output: 
```
{
    "Response": {
        "RequestId": "14e70aa5-d247-47a2-ba74-d67f5d05956b",
        "SecurityGroupPolicy": [
            {
                "Action": "ACCEPT",
                "AddressTemplate": {
                    "AddressGroupId": "",
                    "AddressId": ""
                },
                "CidrBlock": "0.0.0.0/0",
                "Direction": "Ingress",
                "Ipv6CidrBlock": "",
                "ModifyTime": "2026-03-27 17:23:58",
                "PolicyDescription": "cdasccsd",
                "PolicyIndex": 0,
                "Port": "ALL",
                "Protocol": "ALL",
                "Region": "ap-shanghai-fsi",
                "SecurityGroupId": "",
                "ServiceTemplate": {
                    "ServiceGroupId": "",
                    "ServiceId": ""
                },
                "Version": "3"
            },
            {
                "Action": "ACCEPT",
                "AddressTemplate": {
                    "AddressGroupId": "",
                    "AddressId": ""
                },
                "CidrBlock": "",
                "Direction": "Ingress",
                "Ipv6CidrBlock": "::/0",
                "ModifyTime": "2026-03-16 17:54:26",
                "PolicyDescription": "",
                "PolicyIndex": 1,
                "Port": "ALL",
                "Protocol": "ALL",
                "Region": "ap-shanghai-fsi",
                "SecurityGroupId": "",
                "ServiceTemplate": {
                    "ServiceGroupId": "",
                    "ServiceId": ""
                },
                "Version": "3"
            }
        ]
    }
}
```

