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
                "Vip": "",
                "Port": [],
                "RiskConfig": [],
                "NameSpace": "",
                "AssetStatus": "RUNNING",
                "AssetEventNum": 5276,
                "GroupName": "全量资产",
                "InstanceId": "ins-07ynpvog",
                "AssetRegionName": "亚太地区(东京)",
                "AssetCspmRiskNum": 16,
                "Status": 0,
                "Region": "",
                "LoadBalancerType": "",
                "RDPRisk": "",
                "SsaAssetDiscoverTime": "2020-03-31 21:35:00",
                "InstanceState": "RUNNING",
                "PublicIpAddresses": [
                    "150.109.204.129"
                ],
                "SSHRisk": "公网开放SSH",
                "CertType": "",
                "Vul": "",
                "ProductType": 0,
                "EventRisk": "",
                "ChargeType": "POSTPAID_BY_HOUR",
                "AssetVpcName": "Default-VPC",
                "SsaAssetDeleteTime": "",
                "AssetIpv6": [],
                "AssetCreateTime": "",
                "LoadBalancerVips": [],
                "CreationDate": "",
                "VpcId": "",
                "AssetType": "cvm",
                "PrivateIpAddresses": [
                    "10.203.0.6"
                ],
                "CertEndTime": "",
                "Name": "测试",
                "Tag": [],
                "DiskSize": 0,
                "AssetUniqid": "",
                "DiskType": "",
                "AssetSubnetId": "subnet-f05xi0dn",
                "Domain": "",
                "Uin": 0,
                "AssetSubnetName": "Default-Subnet",
                "EngineVersion": "",
                "Event": "",
                "ClusterType": 0,
                "AssetVpcid": "vpc-pndhl438",
                "ValidityPeriod": ""
            }
        ],
        "Total": 623,
        "RequestId": "a60a394d-0993-4ded-b422-c0e019fb13ea"
    }
}
```

