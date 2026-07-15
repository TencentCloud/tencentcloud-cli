**Example 1: 查询已经接入waf的clb信息**



Input: 

```
tccli waf DescribeCLBObjects --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --WafAccess True
```

Output: 
```
{
    "Response": {
        "ClbObjects": [
            {
                "AddTime": "2026-05-09 19:54:17",
                "ClsStatus": 0,
                "InstanceId": "waf_2kzgm3ei00pk7563",
                "InstanceLevel": 4,
                "InstanceName": "zhenhuatest",
                "IpHeaders": [],
                "MemberAppId": 251254511,
                "MemberUin": "700000916577",
                "ModifyTime": "2026-05-10 13:33:02",
                "NumericalVpcId": 11533948,
                "ObjectFlowMode": 1,
                "ObjectId": "lb-09p2rkxs",
                "ObjectName": "rrrrrrrtest1736993464_jbv20",
                "PostCKafkaStatus": 0,
                "PostCLSStatus": 0,
                "PreciseDomainDetails": [
                    {
                        "AccessStatus": 1,
                        "AlbType": "clb",
                        "ApiStatus": 0,
                        "AppId": 251254511,
                        "BotStatus": 0,
                        "CCList": [],
                        "CdcClusters": "",
                        "CloudType": "",
                        "ClsStatus": 0,
                        "Cname": "",
                        "CreateTime": "2026-05-09 19:54:17",
                        "Domain": "lb-09p2rkxs.clb-default.qcloudwaf.com",
                        "DomainId": "lb-09p2rkxs",
                        "Edition": "clb-waf",
                        "Engine": 0,
                        "FlowMode": 1,
                        "InstanceId": "waf_2kzgm3ei00pk7563",
                        "InstanceName": "zhenhuatest",
                        "Ipv6Status": 0,
                        "IsREIP": 0,
                        "LLMStatus": 0,
                        "Labels": [],
                        "Level": 0,
                        "LoadBalancerSet": [],
                        "Mode": 0,
                        "Note": "",
                        "Ports": [],
                        "PostCKafkaStatus": 0,
                        "PostCLSStatus": 0,
                        "PrivateVipStatus": 0,
                        "REIPObjectId": "",
                        "Region": "gz",
                        "RsList": [],
                        "SgDetail": "",
                        "SgID": "",
                        "SgState": 0,
                        "SrcList": [],
                        "State": 0,
                        "Status": 1,
                        "UpstreamDomainList": [],
                        "Vip": "172.16.49.139"
                    }
                ],
                "PreciseDomains": [],
                "PrivateIp": [
                    "172.16.49.139"
                ],
                "PublicIp": [],
                "Region": "gz",
                "Status": 1,
                "Type": "CLB",
                "VirtualDomain": "lb-09p2rkxs.clb-default.qcloudwaf.com",
                "Vpc": "vpc-2tjdmcp3",
                "VpcName": "Default-VPC",
                "WafAccessStatus": 1
            }
        ],
        "TotalCount": 12,
        "RequestId": "041fbbc9-0546-4ab4-9f14-3a7cdaa0a16d"
    }
}
```

