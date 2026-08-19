**Example 1: 全部资产**



Input: 

```
tccli csip DescribeCloudAssets --cli-unfold-argument  \
    --MemberId mem-0acb10f2*9*****e \
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
                "Text": "其他环境-集群节点",
                "Value": "other-node"
            }
        ],
        "Assets": [
            {
                "AlarmCount": 0,
                "AppID": 1300448058,
                "AssetID": "AKID********rPkusc9TaUBVpzwgGfrr3GKB",
                "AssetName": "AKID********rPkusc9TaUBVpzwgGfrr3GKB",
                "AssetRID": "dae77*f9092d*b**ed**9efd27d4cbd6",
                "AssetStatus": "active",
                "AssetType": "cam_user_ak",
                "AssetTypeName": "CAM 用户密钥",
                "CloudAccountID": "10*0*1*16646",
                "CloudAccountName": "天***",
                "CreatedAt": "2026-02-02T21:01:22+08:00",
                "CriticalRiskCount": 0,
                "CustomTags": [],
                "FirstSyncTime": "2026-02-03T00:20:35+08:00",
                "HighRiskCount": 0,
                "LowRiskCount": 0,
                "MediumRiskCount": 0,
                "OsName": "",
                "PrivateDomain": "",
                "PrivateIP": "",
                "ProtectStatus": 0,
                "Provider": "tencent",
                "ProviderName": "腾讯云",
                "PublicDomain": "",
                "PublicExpose": 0,
                "PublicIP": "",
                "Region": "",
                "RegionName": "",
                "RiskCount": 0,
                "Tags": [],
                "UpdateTime": "2026-02-05T16:09:11+08:00"
            }
        ],
        "TotalCount": 3024,
        "RequestId": "1b3622b8-01d6-4f53-af0a-69a277a934c3"
    }
}
```

