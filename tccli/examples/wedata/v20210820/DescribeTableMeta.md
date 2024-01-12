**Example 1: 查询表元数据详情**



Input: 

```
tccli wedata DescribeTableMeta --cli-unfold-argument  \
    --TableId 12345
```

Output: 
```
{
    "Response": {
        "TableMeta": {
            "ClusterId": "xx",
            "TableHeat": {
                "Heat": 0.0,
                "TableId": "xx",
                "DayTime": "2020-09-22T00:00:00+00:00"
            },
            "DatabaseId": "xx",
            "HasFavorite": true,
            "ProjectDisplayName": "xx",
            "StorageSizeWithUnit": "xx",
            "TableId": "xx",
            "BizCatalogNames": [
                "xx"
            ],
            "TablePath": "xx",
            "LikeCount": 0,
            "TableNameCn": "xx",
            "DdlModifyTime": "2020-09-22T00:00:00+00:00",
            "Description": "xx",
            "InstanceId": "xx",
            "TableName": "xx",
            "LastAccessTime": "2020-09-22T00:00:00+00:00",
            "LifeCycleTime": 0,
            "MetastoreId": 0,
            "DataModifyTime": "2020-09-22T00:00:00+00:00",
            "TablePropertyScore": {
                "Timeliness": 0.0,
                "Average": 0.0,
                "DayTime": "2020-09-22T00:00:00+00:00",
                "Normative": 0.0,
                "Stability": 0.0,
                "TableId": "xx",
                "Safety": 0.0,
                "Integrity": 0.0
            },
            "Partitions": "xx",
            "ReplicationFactor": "xx",
            "DatasourceName": "xx",
            "StorageFormat": "xx",
            "TechnologyType": "xx",
            "ProjectId": "xx",
            "BizCatalogIds": [
                "xx"
            ],
            "ColumnSeparator": "xx",
            "DatasourceId": 0,
            "HasAdminAuthority": true,
            "TableOwnerName": "xx",
            "ModifyTime": "2020-09-22T00:00:00+00:00",
            "TableNameEn": "xx",
            "FavoriteCount": 0,
            "TableType": "xx",
            "DatasourceDisplayName": "xx",
            "ClusterName": "xx",
            "ProjectName": "xx",
            "HasLike": true,
            "MetastoreType": "xx",
            "DatabaseName": "xx",
            "StorageSize": 0,
            "CreateTime": "2020-09-22T00:00:00+00:00"
        },
        "RequestId": "xx"
    }
}
```

