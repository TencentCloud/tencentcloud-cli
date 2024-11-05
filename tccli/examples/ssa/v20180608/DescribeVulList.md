**Example 1: 资产中心漏洞管理页漏洞列表**



Input: 

```
tccli ssa DescribeVulList --cli-unfold-argument  \
    --Params { "FilterObj": { "VulId": [ "101741" ] }, "Limit": 10, "Page": 1, "By": "event_time", "Order": "desc" }
```

Output: 
```
{
    "Response": {
        "Data": {
            "List": [
                {
                    "Id": "100023",
                    "VulName": "vul name",
                    "Type": 0,
                    "Level": 0,
                    "Status": 0,
                    "Time": "2020-10-10 12:12:12",
                    "ImpactAssetNum": 0,
                    "ImpactAsset": "asset",
                    "ImpactAssetName": "name",
                    "VulDetail": "vul detail info",
                    "VulRefLink": "http://excample.com",
                    "OldIdMd5": "md5****",
                    "UniqId": "456d***",
                    "OperateTime": "2020-10-10 12:12:12",
                    "IsAssetDeleted": "0",
                    "DiscoverTime": "2020-10-10 12:12:12",
                    "OriginId": 1,
                    "Region": "ap-guangzhou",
                    "Vpcid": "vpc-***",
                    "AssetType": "cvm",
                    "AssetSubType": "1",
                    "AssetIpAll": [
                        "10.0.1.1",
                        "10.0.1.2"
                    ],
                    "PublicIpAddresses": [
                        "132.*.*.*"
                    ],
                    "PrivateIpAddresses": [
                        "10.0.0.1"
                    ],
                    "VulSource": "nvd",
                    "AffectedUrl": "http://excample.com",
                    "SsaAssetCategory": 0,
                    "VulUrl": "http://excample.com",
                    "IsOpen": true,
                    "YzHostId": 1,
                    "VulRepairPlan": "repari plan info",
                    "VulPath": "/use/bin/nginx"
                }
            ],
            "Total": 1
        },
        "RequestId": "f9184c15-9721-456d-8ca0-4263967b5ead"
    }
}
```

