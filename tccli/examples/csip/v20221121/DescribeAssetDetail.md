**Example 1: 资产详情**



Input: 

```
tccli csip DescribeAssetDetail --cli-unfold-argument  \
    --AssetID sg-2uztgeed \
    --Provider tencent \
    --AssetType security_group
```

Output: 
```
{
    "Response": {
        "AssetDetail": {
            "AlarmCount": 0,
            "AppID": 1300440050,
            "AssetID": "sg-2*z*geed",
            "AssetName": "放通全部端口",
            "AssetRID": "fbe6034*9089*8*ce9fc6217e4feb398",
            "AssetType": "security_group",
            "AssetTypeIconURL": "https://cloud-xspm*web-1258344699.cos.ap-g*angzhou.myqcloud.com/as*et-icon/networkingIcon_3d.*n*",
            "AssetTypeName": "安全组",
            "CloudAccountName": "天空之蓝",
            "CustomTags": [],
            "PrivateDomain": "t.w**.c*m",
            "PrivateIP": "10.0.0.0",
            "Provider": "tencent",
            "PublicDomain": "t.com",
            "PublicIP": "1.0.0.0",
            "RiskCount": 2,
            "SecurityGroupIDs": [
                "sg-2uztgeed"
            ],
            "Tags": []
        },
        "DetailTabs": [
            "risk"
        ],
        "DynamicTabs": [
            {
                "Count": 2,
                "TabKey": "risk"
            }
        ],
        "RequestId": "ef89687f-ff7b-4a9c-9c9a-e8cc6d4a4e8f"
    }
}
```

