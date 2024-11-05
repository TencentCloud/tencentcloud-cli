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
                    "AssetType": "Instance",
                    "Name": "andy",
                    "AssetRegionName": "guangzhou",
                    "AssetVpcid": "vpc-ssr158",
                    "InstanceType": "CVM",
                    "InstanceState": "running",
                    "EngineVersion": "1.0.15",
                    "Id": "id-ssr",
                    "Tag": [
                        {
                            "Fid": 0,
                            "Fname": "fandy"
                        }
                    ],
                    "AssetCspmRiskNum": 0,
                    "PublicIpAddresses": [
                        "10.13.***.1"
                    ],
                    "AssetUniqid": "3cbf2d8f-c40a-452a-92ec-140f9b2d29a2",
                    "ChargeType": "forward",
                    "AssetEventNum": 0,
                    "AssetVulNum": 0,
                    "PrivateIpAddresses": [
                        "172.**.11.1"
                    ],
                    "GroupName": "group-andy",
                    "SsaAssetDiscoverTime": "2016-10-31 19:46:48",
                    "SsaAssetDeleteTime": "2016-10-31 19:46:48",
                    "IsNew": true,
                    "AssetSubnetId": "subnet-112ssr",
                    "AssetSubnetName": "subnet-andy",
                    "AssetVpcName": "vpc-andy",
                    "ClusterType": 0,
                    "NameSpace": "default",
                    "LoadBalancerType": "clb",
                    "LoadBalancerVips": [
                        "172.*.12.**"
                    ],
                    "AssetIpv6": [
                        "6bb56a09278740bc80c5dc6dab783eff"
                    ],
                    "SSHRisk": "risk ssh",
                    "RDPRisk": "risk rdb",
                    "EventRisk": "risk event"
                }
            ]
        },
        "AggregationData": [
            {
                "Type": "AssetRegionName",
                "Bucket": [
                    {
                        "Key": "guangzhou",
                        "Count": 10
                    }
                ]
            }
        ],
        "NamespaceData": [
            "sec"
        ],
        "RequestId": "3cbf2d8f-c40a-452a-92ec-140f9b2d29a2"
    }
}
```

