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
            "ProductType": null,
            "AssetStatus": "运行中",
            "AssetType": "cvm",
            "Id": "1445149556-cvm-ins-3o0cn0bo",
            "Tag": [
                {
                    "Fname": "test1",
                    "Fid": 255
                },
                {
                    "Fname": "test2",
                    "Fid": 256
                },
                {
                    "Fname": "dasd",
                    "Fid": 257
                },
                {
                    "Fname": "222",
                    "Fid": 258
                }
            ],
            "Name": "云鼎-张云飞-LINUX测试",
            "AssetUniqid": "ins-3o0cn0bo",
            "InstanceType": "I2.MEDIUM4",
            "InstanceState": "RUNNING",
            "PublicIpAddresses": [
                "118.89.39.26"
            ],
            "PrivateIpAddresses": [
                "10.104.119.159"
            ],
            "EngineVersion": "",
            "Vip": "10.104.119.159",
            "Status": null,
            "LoadBalancerVips": null,
            "Uin": null,
            "CreationDate": null,
            "Domain": null,
            "InstanceId": "ins-3o0cn0bo",
            "DiskType": null,
            "DiskSize": null,
            "CertType": null,
            "ProjectName": "",
            "CertEndTime": null,
            "ValidityPeriod": null,
            "SsaAssetDiscoverTime": "2020-03-31 21:34:55",
            "AssetSubnetId": "",
            "AssetSubnetName": "",
            "AssetVpcName": "",
            "ClusterType": 0,
            "NameSpace": "",
            "AssetCreateTime": "",
            "LoadBalancerType": null,
            "AssetIpv6": [],
            "AssetVulNum": 0,
            "GroupName": "",
            "Port": [
                "http(8080)",
                "http(80)"
            ],
            "RiskConfig": [
                "安全组配置",
                "主机安全防护状态",
                "密钥对登陆"
            ],
            "Event": "[{\"key\":\"11\",\"doc_count\":1334}]",
            "Vul": "[]",
            "SSHRisk": "",
            "RDPRisk": "",
            "EventRisk": "资产失陷"
        },
        "RequestId": "f86588f7-fb1f-4fdd-9c8b-c882f044eeb0"
    }
}
```

