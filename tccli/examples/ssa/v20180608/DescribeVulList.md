**Example 1: 资产中心漏洞管理页漏洞列表**



Input: 

```
tccli ssa DescribeVulList --cli-unfold-argument  \
    --Params xxx
```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                {
                    "Id": "abc",
                    "VulName": "abc",
                    "Type": 0,
                    "Level": 0,
                    "Status": 0,
                    "Time": "abc",
                    "ImpactAssetNum": 0,
                    "ImpactAsset": "abc",
                    "ImpactAssetName": "abc",
                    "VulDetail": "abc",
                    "VulRefLink": "abc",
                    "OldIdMd5": "abc",
                    "UniqId": "abc",
                    "OperateTime": "abc",
                    "IsAssetDeleted": "abc",
                    "DiscoverTime": "abc",
                    "OriginId": 1,
                    "Region": "abc",
                    "Vpcid": "abc",
                    "AssetType": "abc",
                    "AssetSubType": "abc",
                    "AssetIpAll": [
                        "abc"
                    ],
                    "PublicIpAddresses": [
                        "abc"
                    ],
                    "PrivateIpAddresses": [
                        "abc"
                    ],
                    "VulSource": "abc",
                    "AffectedUrl": "abc",
                    "SsaAssetCategory": 0,
                    "VulUrl": "abc",
                    "IsOpen": true,
                    "YzHostId": 1,
                    "VulRepairPlan": "abc",
                    "VulPath": "abc"
                }
            ],
            "Total": 0
        },
        "RequestId": "abc"
    }
}
```

