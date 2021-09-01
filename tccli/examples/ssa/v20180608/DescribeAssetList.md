**Example 1: 资产安全资产列表**



Input: 

```
tccli ssa DescribeAssetList --cli-unfold-argument  \
    --Params {"Limit":10,"Order":"desc","By":"field","Page":1,"FilterObj":{"AssetIpAll":[],"AssetName":[],"AssetRegionName":[],"AssetType":[],"AssetUniqid":[],"AssetVpcid":[],"NameSpace":[],"Tag":[],"RiskTag":""}}
```

Output: 
```
{
    "Response": {
        "AssetList": {
            "Total": 1,
            "List": [
                {
                    "AssetType": "repository",
                    "Id": "1445149556-repository-tstsec/test",
                    "Tag": [
                        {
                            "Fname": "test2",
                            "Fid": 256
                        }
                    ],
                    "Name": "test",
                    "AssetRegionName": "东南亚地区(新加坡)",
                    "AssetVpcid": "",
                    "InstanceType": "",
                    "InstanceState": "",
                    "PublicIpAddresses": [],
                    "PrivateIpAddresses": [],
                    "EngineVersion": "",
                    "AssetUniqid": "tstsec/test",
                    "ChargeType": "",
                    "AssetCspmRiskNum": 1,
                    "AssetVulNum": 0,
                    "AssetEventNum": 0,
                    "SsaAssetDiscoverTime": "2020-05-12 20:07:06",
                    "SsaAssetDeleteTime": "",
                    "GroupName": "",
                    "AssetSubnetId": "",
                    "AssetSubnetName": "",
                    "AssetVpcName": "",
                    "ClusterType": 0,
                    "NameSpace": "tstsec",
                    "IsNew": false,
                    "LoadBalancerType": "xx",
                    "LoadBalancerVips": [
                        "xx",
                        "xx"
                    ],
                    "AssetIpv6": [
                        "xx",
                        "xx"
                    ],
                    "SSHRisk": "xx",
                    "RDPRisk": "xx",
                    "EventRisk": "xx"
                }
            ]
        },
        "AggregationData": [
            {
                "Type": "AssetRegionName",
                "Bucket": [
                    {
                        "Key": "华南地区(广州)",
                        "Count": 305
                    },
                    {
                        "Key": "华东地区(上海)",
                        "Count": 43
                    },
                    {
                        "Key": "东南亚地区(香港)",
                        "Count": 30
                    },
                    {
                        "Key": "华北地区(北京)",
                        "Count": 26
                    },
                    {
                        "Key": "西南地区(成都)",
                        "Count": 21
                    },
                    {
                        "Key": "",
                        "Count": 20
                    },
                    {
                        "Key": "东南亚地区(新加坡)",
                        "Count": 9
                    },
                    {
                        "Key": "美国西部(硅谷)",
                        "Count": 9
                    },
                    {
                        "Key": "欧洲地区(法兰克福)",
                        "Count": 8
                    },
                    {
                        "Key": "亚太地区(首尔)",
                        "Count": 7
                    },
                    {
                        "Key": "华南地区(深圳金融)",
                        "Count": 5
                    },
                    {
                        "Key": "亚太地区(东京)",
                        "Count": 4
                    },
                    {
                        "Key": "美国东部(弗吉尼亚)",
                        "Count": 4
                    },
                    {
                        "Key": "亚太地区(曼谷)",
                        "Count": 3
                    },
                    {
                        "Key": "亚太地区(孟买)",
                        "Count": 2
                    },
                    {
                        "Key": "北美地区(多伦多)",
                        "Count": 2
                    },
                    {
                        "Key": "欧洲地区(莫斯科)",
                        "Count": 2
                    },
                    {
                        "Key": "华南地区(广州Open)",
                        "Count": 1
                    },
                    {
                        "Key": "西南地区(重庆)",
                        "Count": 1
                    }
                ]
            }
        ],
        "NamespaceData": [
            "test12",
            "testsoc",
            "tstsec"
        ],
        "RequestId": "e1fea906-cdcc-44fa-aa26-3d9397a98a5c"
    }
}
```

