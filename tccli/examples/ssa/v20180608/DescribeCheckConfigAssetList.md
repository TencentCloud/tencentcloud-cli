**Example 1: 云安全配置管理资产组列表**



Input: 

```
tccli ssa DescribeCheckConfigAssetList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 1 \
    --Id 17a5c13d-f95d-4065-8e7d-33b6b56e71b5
```

Output: 
```
{
    "Response": {
        "Total": 100,
        "CheckAssetsList": [
            {
                "Id": 1325870,
                "Instid": "didi-1251001047",
                "Taskid": "1066159338",
                "AssetId": "1445149556-cos-didi-1251001047",
                "Result": 2,
                "Url": "https://console.cloud.tencent.com/cos5/bucket/setting?type=aclconfig&bucketName=didi-1251001047&projectId=0&path=%252F&region=ap-chengdu",
                "IsIgnore": 0,
                "IsChecked": 1,
                "Updatetime": "2020-08-07 00:16:59",
                "AssetInfo": "{\"AssetCreateTime\":\"2018-02-26 16:48:51\",\"AssetIpAll\":[],\"CreationDate\":\"2018-02-26T08:48:51Z\",\"AssetEventNum\":0,\"AssetIpv6\":[],\"AssetRegion\":\"ap-chengdu\",\"AssetStatus\":\"\",\"SsaUid\":\"1445149556\",\"AssetUniqid\":\"didi-1251001047\",\"AssetStatusName\":\"\",\"AssetVpcName\":\"\",\"Name\":\"didi-1251001047\",\"AssetVpcid\":\"\",\"AssetRiskTotalNum\":4,\"AssetProjectName\":\"\",\"SsaAssetDiscoverTime\":\"2020-04-15 15:09:28\",\"AssetRegionName\":\"西南地区(成都)\",\"AssetSubType\":\"cos\",\"AssetCspmRiskNum\":4,\"AssetVersion\":11637,\"SsaLogTime\":1596727246000,\"AssetName\":\"didi-1251001047\",\"AssetType\":\"cos\",\"AssetVulNum\":0,\"AssetInnerType\":\"\",\"AssetSubnetId\":\"\",\"AssetVip\":\"\",\"Region\":\"ap-chengdu\",\"AssetShow\":\"1\",\"AssetSubnetName\":\"\",\"AssetUid\":\"1445149556\",\"Domain\":\"didi-1251001047.cos.ap-chengdu.myqcloud.com\",\"AssetUpdateTime\":\"2020-08-06 23:20:46\"}",
                "Detail": "开放了公有读权限",
                "Tag": "[]"
            }
        ],
        "RequestId": "d4d1e94d-430e-4bc7-9c10-a84f0685e366"
    }
}
```

