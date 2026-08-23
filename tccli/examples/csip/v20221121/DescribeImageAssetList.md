**Example 1: 查询镜像资产列表**



Input: 

```
tccli csip DescribeImageAssetList --cli-unfold-argument  \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "ImageList": [
            {
                "CriticalLevelVulCnt": 0,
                "HighLevelVulCnt": 0,
                "Id": "802",
                "ImageCreateTime": "2026-04-07T11:07:15+08:00",
                "ImageDigest": "sha256:0074e38a3b63c1768b964b7dfd194cae98a528aafb71b870a230ea23470e1503",
                "ImageId": "sha256:048a5bc1641e14f0884742973c842a640e4010883491c5ef79723a8de6fce388",
                "ImageName": "yancyw",
                "ImageRepoAddress": "ccr.ccs.tencentyun.com/csip/yancyw",
                "ImageSize": 125067215,
                "ImageTag": "qinglong",
                "InstanceId": "tcr-instance",
                "InstanceName": "ccr-sa-saopaulo",
                "IsAuthorized": 0,
                "IsLatestImage": false,
                "LatestScanTime": "2026-06-29T10:45:14+08:00",
                "LowLevelVulCnt": 0,
                "MediumLevelVulCnt": 0,
                "Namespace": "csip",
                "OwnerAccountName": "700002365149",
                "OwnerAppId": 260083796,
                "OwnerUin": "700002365149",
                "RegistryRegion": "sa-saopaulo",
                "ScanStatus": 0,
                "SensitiveCnt": 0,
                "VirusCnt": 0,
                "VulCnt": 0
            }
        ],
        "TotalCount": 287,
        "RequestId": "8411b494-84eb-4af3-aac1-dae15d54bf9e"
    }
}
```

