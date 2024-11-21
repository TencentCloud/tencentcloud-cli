**Example 1: 漏洞影响主机列表**

漏洞影响主机列表

Input: 

```
tccli cwp DescribeVulEffectHostList --cli-unfold-argument  \
    --VulId 100435 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "4234234",
        "TotalCount": 2,
        "VulEffectHostList": [
            {
                "EventId": 15,
                "FirstDiscoveryTime": "2021-03-24 16:37:57",
                "MachineExtraInfo": {
                    "WanIP": "10.0.1****",
                    "PrivateIP": "10.0.1****",
                    "NetworkType": 0,
                    "NetworkName": "vpc-3gov****",
                    "InstanceID": "lhins-n4sz****",
                    "HostName": "demo_****"
                },
                "PublicIpAddresses": "1.1.1.1",
                "InstanceState": "PENDING",
                "IsSupportAutoFix": 2,
                "HostVersion": 101,
                "CloudTags": [
                    {
                        "TagKey": "Dev",
                        "TagValue": "cwp"
                    }
                ],
                "Description": "说明信息",
                "FixStatusMsg": "修复超时",
                "Status": 0,
                "LastTime": "2020-04-22 03:29:52",
                "Level": 1,
                "Quuid": "b86925b4-cc36-420e-80d4-5094cb2f094b",
                "Uuid": "ed629672-165e-11ea-8bcf-40f2e9f3d932",
                "HostIp": "10.104.14.165",
                "AliasName": "poc测试(129.204.36.227)",
                "Tags": [
                    "cwp"
                ]
            }
        ]
    }
}
```

