**Example 1: DescribeAssetDetailList**



Input: 

```
tccli ssa DescribeAssetDetailList --cli-unfold-argument  \
    --PageIndex 0 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ProjectName": "默认项目",
                "Id": "ins-07ynpvog",
                "InstanceType": "S2.SMALL1",
                "AssetVulNum": 2,
                "Vip": "172.***.11.**",
                "Port": [
                    "http(8080)",
                    "http(80)"
                ],
                "RiskConfig": [
                    "安全组配置",
                    "主机安全防护状态",
                    "密钥对登陆"
                ],
                "NameSpace": "default",
                "AssetStatus": "RUNNING",
                "AssetEventNum": 5276,
                "GroupName": "全量资产",
                "InstanceId": "ins-07ynpvog",
                "AssetRegionName": "亚太地区(东京)",
                "AssetCspmRiskNum": 16,
                "Status": 0,
                "Region": "ap-guangzhou",
                "LoadBalancerType": "clb",
                "RDPRisk": "risk rdb",
                "SsaAssetDiscoverTime": "2020-03-31 21:35:00",
                "InstanceState": "RUNNING",
                "PublicIpAddresses": [
                    "150.109.204.129"
                ],
                "SSHRisk": "公网开放SSH",
                "CertType": "https",
                "Vul": "vul",
                "ProductType": 0,
                "EventRisk": "risk event",
                "ChargeType": "POSTPAID_BY_HOUR",
                "AssetVpcName": "Default-VPC",
                "SsaAssetDeleteTime": "2020-04-31 21:34:55",
                "AssetIpv6": [
                    "ipv6"
                ],
                "AssetCreateTime": "2020-04-31 21:34:55",
                "LoadBalancerVips": [
                    "ip1"
                ],
                "CreationDate": "2020-04-31 21:34:55",
                "VpcId": "vpc-9527",
                "AssetType": "cvm",
                "PrivateIpAddresses": [
                    "10.203.0.6"
                ],
                "CertEndTime": "2020-03-31 21:34:55",
                "Name": "Name1",
                "Tag": [
                    {
                        "Fname": "tag1",
                        "Fid": 255
                    },
                    {
                        "Fname": "tag2",
                        "Fid": 256
                    }
                ],
                "DiskSize": 0,
                "AssetUniqid": "ins-3o0cn0bo",
                "DiskType": "ssd",
                "AssetSubnetId": "subnet-f05xi0dn",
                "Domain": "domain",
                "Uin": 0,
                "AssetSubnetName": "Default-Subnet",
                "EngineVersion": "12.1.1",
                "Event": "event",
                "ClusterType": 0,
                "AssetVpcid": "vpc-pndhl438",
                "ValidityPeriod": "day"
            }
        ],
        "Total": 62,
        "RequestId": "a60a394d-0993-4ded-b422-c0e019fb13ea"
    }
}
```

