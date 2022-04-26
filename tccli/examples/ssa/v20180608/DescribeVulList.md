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
            "Total": 0,
            "List": [
                {
                    "VulDetail": "xx",
                    "AssetSubType": "xx",
                    "VulSource": "xx",
                    "VulRepairPlan": "xx",
                    "ImpactAsset": "xx",
                    "IsAssetDeleted": "xx",
                    "Type": 0,
                    "Status": 0,
                    "VulUrl": "xx",
                    "VulRefLink": "xx",
                    "VulName": "xx",
                    "SsaAssetCategory": 0,
                    "UniqId": "xx",
                    "AssetType": "xx",
                    "Vpcid": "xx",
                    "OldIdMd5": "xx",
                    "DiscoverTime": "xx",
                    "Level": 0,
                    "ImpactAssetName": "xx",
                    "Region": "xx",
                    "PrivateIpAddresses": [
                        "xx"
                    ],
                    "Time": "xx",
                    "OriginId": 1,
                    "PublicIpAddresses": [
                        "xx"
                    ],
                    "YzHostId": 1,
                    "AffectedUrl": "xx",
                    "IsOpen": true,
                    "OperateTime": "xx",
                    "AssetIpAll": [
                        "xx"
                    ],
                    "ImpactAssetNum": 0,
                    "VulPath": "xx",
                    "Id": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

