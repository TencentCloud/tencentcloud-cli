**Example 1: 查询镜像仓库组件关联镜像列表**



Input: 

```
tccli csip DescribeAssetComponentRelatedImageList --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Id 1
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
                "ImageRepoAddress": "ccr.ccs.tencentyun.com/****/******",
                "ImageSize": 125067215,
                "ImageTag": "qi******",
                "InstanceId": "tcr-instance",
                "InstanceName": "ccr-sa-saopaulo",
                "IsAuthorized": 1,
                "IsLatestImage": false,
                "LatestScanTime": "2026-07-01T11:59:34+08:00",
                "LowLevelVulCnt": 0,
                "MediumLevelVulCnt": 0,
                "Namespace": "csip",
                "OwnerAccountName": "70000*******",
                "OwnerAppId": 260000000,
                "OwnerUin": "70000*******",
                "RegistryRegion": "sa-saopaulo",
                "ScanStatus": 10,
                "SensitiveCnt": 0,
                "VirusCnt": 0,
                "VulCnt": 0
            }
        ],
        "TotalCount": 1,
        "RequestId": "814ca926-af90-42f1-80fd-db1db47b4f7c"
    }
}
```

