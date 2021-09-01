**Example 1: 合规管理资产列表**



Input: 

```
tccli ssa DescribeComplianceAssetList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Id 17a5c13d-f95d-4065-8e7d-33b6b56e71b5
```

Output: 
```
{
    "Response": {
        "Total": 143,
        "CheckAssetsList": [
            {
                "Id": 1304422,
                "Instid": "disk-f7av4ero",
                "Taskid": "1053388124",
                "AssetId": "1445149556-cbs-disk-f7av4ero",
                "Result": 2,
                "IsChecked": 1,
                "Url": "https://console.cloud.tencent.com/cvm/cbs/detail?rid=5&id=disk-f7av4ero",
                "IsIgnore": 0,
                "Updatetime": "2020-08-05 01:38:41",
                "AssetInfo": "{\"AssetCspmRiskNum\":1,\"AssetEventNum\":0,\"AssetInnerType\":\"\",\"AssetIpAll\":[],\"AssetIpv6\":[],\"AssetName\":\"vulcan-cloudsec_0\",\"AssetProjectName\":\"\",\"AssetRegion\":\"ap-hongkong\",\"AssetRegionName\":\"东南亚地区(香港)\",\"AssetRiskTotalNum\":1,\"AssetShow\":\"1\",\"AssetStatus\":\"ATTACHED\",\"AssetStatusName\":\"已挂载\",\"AssetSubType\":\"cbs\",\"AssetSubnetId\":\"\",\"AssetSubnetName\":\"\",\"AssetType\":\"cbs\",\"AssetUid\":\"1445149556\",\"AssetUniqid\":\"disk-f7av4ero\",\"AssetUpdateTime\":\"2020-08-05 00:50:02\",\"AssetVersion\":10521,\"AssetVip\":\"\",\"AssetVpcName\":\"\",\"AssetVpcid\":\"\",\"AssetVulNum\":0,\"Attached\":true,\"AutoRenewFlagError\":false,\"BackupDisk\":false,\"CreateTime\":\"2017-08-24 14:58:23\",\"DeadlineError\":false,\"DeadlineTime\":\"2021-11-24 14:58:26\",\"DeleteWithInstance\":false,\"DifferDaysOfDeadline\":476,\"DiskChargeType\":\"PREPAID\",\"DiskId\":\"disk-f7av4ero\",\"DiskName\":\"vulcan-cloudsec_0\",\"DiskSize\":20,\"DiskState\":\"ATTACHED\",\"DiskType\":\"CLOUD_BASIC\",\"DiskUsage\":\"DATA_DISK\",\"Encrypt\":false,\"InstanceId\":\"ins-bv9hiaek\",\"InstanceIdList\":[\"ins-bv9hiaek\"],\"IsReturnable\":true,\"MigratePercent\":0,\"Migrating\":false,\"Placement\":{\"CageId\":\"\",\"CdcId\":\"\",\"CdcName\":\"\",\"ProjectId\":1020665,\"Zone\":\"ap-hongkong-1\"},\"Portable\":true,\"RenewFlag\":\"NOTIFY_AND_MANUAL_RENEW\",\"ReturnFailCode\":0,\"RollbackPercent\":0,\"Rollbacking\":false,\"Shareable\":false,\"SnapshotAbility\":true,\"SnapshotCount\":0,\"SnapshotSize\":0,\"SsaAssetDiscoverTime\":\"2020-05-28 15:59:20\",\"SsaLogTime\":1596559802000,\"SsaUid\":\"1445149556\"}",
                "Detail": "当前云硬盘自动快照功能未开启",
                "Tag": "[]"
            }
        ],
        "RequestId": "7cf496ff-300a-4454-a995-0cde2961a99d"
    }
}
```

