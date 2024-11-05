**Example 1: 资产安全页资产详情**



Input: 

```
tccli ssa DescribeAssetDetail --cli-unfold-argument  \
    --Params {"id":"xxx"}
```

Output: 
```
{
    "Response": {
        "Data": {
            "Region": "华南地区(广州)",
            "VpcId": "基础网络",
            "ProductType": 1,
            "AssetStatus": "运行中",
            "AssetType": "cvm",
            "Id": "1445149556-cvm-ins-3o0cn0bo",
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
            "Name": "云鼎-LINUX",
            "AssetUniqid": "ins-3o0cn0bo",
            "InstanceType": "I2.MEDIUM4",
            "InstanceState": "RUNNING",
            "PublicIpAddresses": [
                "118.**.39.**"
            ],
            "PrivateIpAddresses": [
                "10.**.**.159"
            ],
            "EngineVersion": "1.2.3",
            "Vip": "10.**.***.159",
            "Status": 1,
            "LoadBalancerVips": [
                "ip1"
            ],
            "Uin": 221426789,
            "CreationDate": "2020-03-31 21:34:55",
            "Domain": "domain",
            "InstanceId": "ins-3o0cn0bo",
            "DiskType": "ssd",
            "DiskSize": 1024,
            "CertType": "https",
            "ProjectName": "project",
            "CertEndTime": "2020-03-31 21:34:55",
            "ValidityPeriod": "day",
            "SsaAssetDiscoverTime": "2020-03-31 21:34:55",
            "AssetSubnetId": "subnet-9527",
            "AssetSubnetName": "sub-andy",
            "AssetVpcName": "vpc-andy",
            "ClusterType": 0,
            "NameSpace": "default",
            "AssetCreateTime": "2020-03-31 21:34:55",
            "LoadBalancerType": "clb",
            "AssetIpv6": [
                "ipv6"
            ],
            "AssetVulNum": 0,
            "GroupName": "group1",
            "AssetEventNum": 10,
            "AssetRegionName": "ap-guangzhou",
            "AssetVpcid": "vpc-9527",
            "SsaAssetDeleteTime": "2020-04-31 21:34:55",
            "AssetCspmRiskNum": 10,
            "ChargeType": "type",
            "Port": [
                "http(8080)",
                "http(80)"
            ],
            "RiskConfig": [
                "安全组配置",
                "主机安全防护状态",
                "密钥对登陆"
            ],
            "Event": "[{\"key\":\"9527\",\"doc_count\":1334}]",
            "Vul": "vul",
            "SSHRisk": "risk ssh",
            "RDPRisk": "risk rdb",
            "EventRisk": "资产失陷"
        },
        "RequestId": "f86588f7-fb1f-4fdd-9c8b-c882f044eeb0"
    }
}
```

