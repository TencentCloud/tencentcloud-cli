**Example 1: 公网资产**



Input: 

```
tccli csip DescribePublicCloudAssets --cli-unfold-argument  \
    --MemberId mem-0acb1**2**a**aee \
    --Limit 1 \
    --Offset 0 \
    --Order UpdateTime \
    --By Desc
```

Output: 
```
{
    "Response": {
        "AssetTypeList": [
            {
                "Text": "腾讯云-负载均衡",
                "Value": "tencent-clb_instance"
            }
        ],
        "Assets": [
            {
                "Address": "1**.17*.1*8.7*",
                "AddressType": "ipv4",
                "AlarmCount": 0,
                "AppID": 1300448058,
                "AssetID": "ins-n**s2b*a",
                "AssetName": "gl测试自动同步",
                "AssetRID": "bb7*7*9*6*c68*2ff48aa1a*7*4***9*",
                "AssetType": "cvm_instance",
                "AssetTypeName": "云服务器",
                "CloudAccountID": "10**11**6*46",
                "CloudAccountName": "天空之蓝",
                "CreatedAt": "2026-01-13T09:17:39+08:00",
                "CriticalRiskCount": 0,
                "CustomTags": [
                    {
                        "TagColor": "red",
                        "TagID": 1,
                        "TagKey": "核心",
                        "TagValue": "核心"
                    }
                ],
                "FirstSyncTime": "2026-01-21T20:04:56+08:00",
                "HighRiskCount": 0,
                "LowRiskCount": 0,
                "MediumRiskCount": 0,
                "ProtectStatus": 1,
                "Provider": "tencent",
                "ProviderName": "腾讯云",
                "Region": "华南地区(广州)",
                "ResolvedAddress": [],
                "RiskCount": 0,
                "Tags": [
                    {
                        "TagKey": "标签产品",
                        "TagValue": "dsad"
                    }
                ],
                "UpdateTime": "2026-02-05T16:09:06+08:00"
            }
        ],
        "RegionList": [
            {
                "Text": "华北地区(北京)",
                "Value": "ap-beijing"
            }
        ],
        "TotalCount": 56,
        "RequestId": "2ce2a61e-56b2-4837-a88c-c0819dd14e5d"
    }
}
```

