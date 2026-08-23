**Example 1: 查询镜像资产详情**



Input: 

```
tccli csip DescribeImageAssetDetail --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Id 802
```

Output: 
```
{
    "Response": {
        "Detail": {
            "Id": "802",
            "ImageCreateTime": "2026-04-07T11:07:15+08:00",
            "ImageDigest": "sha256:0074e38a3b63c1768b964b7dfd194cae98a528aafb71b870a230ea23470e1503",
            "ImageId": "sha256:048a5bc1641e14f0884742973c842a640e4010883491c5ef79723a8de6fce388",
            "ImageName": "yanc**",
            "ImageRepoAddress": "ccr.ccs.tencentyun.com/****/******",
            "ImageSize": 125067215,
            "ImageTag": "qi******",
            "InstanceId": "",
            "InstanceName": "ccr-sa-********",
            "IsAuthorized": 0,
            "Namespace": "csip",
            "OwnerAccountName": "70000*******",
            "OwnerAppId": 260000000,
            "OwnerUin": "7000********",
            "RegistryRegion": "sa-********",
            "RegistryType": "ccr",
            "ScanStatus": 0,
            "SensitiveCnt": 0,
            "VirusCnt": 0,
            "VulCnt": 0
        },
        "RequestId": "200c0a7f-83b2-48df-8ec7-87a62e344cce"
    }
}
```

