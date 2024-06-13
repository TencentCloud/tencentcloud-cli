**Example 1: 查询表元数据详情**



Input: 

```
tccli wedata DescribeTableMeta --cli-unfold-argument  \
    --TableId MvNP9ruUR4qOYfQsaabbcc
```

Output: 
```
{
    "Response": {
        "RequestId": "0eeb0618-621a-4e21-a74d-68f1d183749d",
        "TableMeta": {
            "BizCatalogIds": null,
            "BizCatalogNames": null,
            "ClusterId": "emr-1cbhbbccdd",
            "ClusterName": "emr-1cbhbbccdd",
            "ColumnSeparator": "Hive默认",
            "Columns": [
                {
                    "ChineseName": null,
                    "ColumnKey": null,
                    "Description": "wwwwww",
                    "IsPartition": false,
                    "Name": "wwwww",
                    "Position": 0,
                    "Type": "tinyint",
                    "CreateTime": "2024-01-08T23:32:51.000+00:00",
                    "DefaultValue": null,
                    "Length": null,
                    "ModifiedTime": "2024-01-08T23:32:51.000+00:00",
                    "Precision": null,
                    "Scale": null
                }
            ],
            "CreateTime": "2023-07-04T16:51:54+08:00",
            "DataModifyTime": null,
            "DataSourceCategory": "CLUSTER",
            "DatabaseId": "dgz--YqoS3aWyUYjKE_QQQ",
            "DatabaseName": "test11",
            "DatasourceDisplayName": "hive_emr-1cbhqqbb.test11",
            "DatasourceId": 30111,
            "DatasourceName": "hive_emr-1cbhqqbb",
            "DdlModifyTime": "2023-07-04T16:51:54+08:00",
            "Description": null,
            "FavoriteCount": 0,
            "HasAdminAuthority": false,
            "HasFavorite": false,
            "HasLike": null,
            "InstanceId": "emr-1cbhqqbb",
            "IsPartitionTable": null,
            "IsView": false,
            "LastAccessTime": "2023-07-04T16:53:42+08:00",
            "LifeCycleTime": null,
            "LikeCount": 0,
            "Location": null,
            "MetaCrawlType": "MANAGED_TABLE",
            "MetastoreId": 128643,
            "MetastoreType": "HIVE",
            "ModifyTime": "2023-07-04T16:51:54+08:00",
            "OwnerProjectId": null,
            "PartitionColumns": null,
            "PartitionExpireDays": null,
            "Partitions": null,
            "ProjectDisplayName": "项目测试",
            "ProjectId": "1728806907743539200",
            "ProjectName": "loader_test",
            "ReplicationFactor": null,
            "StorageFormat": "TEXTFILE",
            "StorageSize": 0,
            "StorageSizeWithUnit": "0B",
            "TableHeat": {
                "DayTime": "2024-04-12T00:00:00+08:00",
                "Heat": 0,
                "MaxHeat": 0,
                "TableId": "MvNP9ruUR4qOYfQsaabbcc"
            },
            "TableId": "MvNP9ruUR4qOYfQsaabbcc",
            "TableName": "aaaa_test2",
            "TableNameCn": null,
            "TableNameEn": null,
            "TableOwnerId": null,
            "TableOwnerName": "shaopenquan",
            "TablePath": "hdfs://172.16.0.7:4007/usr/hive/warehouse/test11.db/aaaa_test2",
            "TablePropertyScore": {
                "Average": 79.5,
                "DayTime": "2024-04-12T00:00:00+08:00",
                "Integrity": 88,
                "Normative": 0,
                "Safety": 30,
                "Stability": 100,
                "TableId": "MvNP9ruUR4qOYfQsVo5dFg",
                "Timeliness": 100
            },
            "TableType": "MANAGED_TABLE",
            "TechnologyType": "HIVE"
        }
    }
}
```

