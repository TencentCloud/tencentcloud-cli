**Example 1: 获取表元数据list**



Input: 

```
tccli wedata DescribeTableMetas --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --Filters.0.Name keywordType \
    --Filters.0.Values table \
    --Filters.1.Name msTypes \
    --Filters.1.Values HIVE HBASE \
    --Filters.2.Name keyword \
    --Filters.2.Values t210011 \
    --OrderFields.0.Name heatValue \
    --OrderFields.0.Direction ASC
```

Output: 
```
{
    "Response": {
        "TableMetas": [
            {
                "ClusterId": null,
                "TableHeat": {
                    "Heat": 0,
                    "MaxHeat": 0,
                    "TableId": "100011eKq1NfbRTkGIhfK_Q",
                    "DayTime": "2020-09-22T00:00:00+00:00"
                },
                "DatabaseId": "12tAIQcu10001_jg",
                "HasFavorite": true,
                "ProjectDisplayName": "dev-proj",
                "StorageSizeWithUnit": "839B",
                "TableId": "100011eKq1NfbRTkGIhfK_Q",
                "BizCatalogNames": [],
                "TablePath": null,
                "LikeCount": 0,
                "TableNameCn": null,
                "DdlModifyTime": "2020-09-22T00:00:00+00:00",
                "Description": null,
                "InstanceId": null,
                "TableName": "t2",
                "LastAccessTime": "2020-09-22T00:00:00+00:00",
                "LifeCycleTime": 0,
                "MetastoreId": 0,
                "DataModifyTime": "2020-09-22T00:00:00+00:00",
                "TablePropertyScore": {
                    "Timeliness": 0,
                    "Average": 0,
                    "DayTime": "2020-09-22T00:00:00+00:00",
                    "Normative": 0,
                    "Stability": 0,
                    "TableId": "100011eKq1NfbRTkGIhfK_Q",
                    "Safety": 0,
                    "Integrity": 0
                },
                "Partitions": null,
                "ReplicationFactor": null,
                "DatasourceName": "hive_emr-db",
                "StorageFormat": null,
                "TechnologyType": null,
                "ProjectId": "1840468646888110001",
                "BizCatalogIds": [],
                "ColumnSeparator": null,
                "DataSourceCategory": null,
                "Columns": [
                    {
                        "ChineseName": null,
                        "ColumnKey": null,
                        "Description": null,
                        "IsPartition": false,
                        "Name": "id",
                        "Position": 0,
                        "Type": "BIGINT",
                        "CreateTime": "2024-01-04T05:51:19.000+00:00",
                        "DefaultValue": null,
                        "Length": null,
                        "ModifiedTime": "2024-01-04T05:51:19.000+00:00",
                        "Precision": null,
                        "Scale": null
                    }
                ],
                "DatasourceId": 0,
                "HasAdminAuthority": true,
                "TableOwnerName": "owner-name",
                "ModifyTime": "2020-09-22T00:00:00+00:00",
                "TableNameEn": "t2",
                "FavoriteCount": 0,
                "TableType": null,
                "DatasourceDisplayName": "hive_emr-bb",
                "ClusterName": null,
                "ProjectName": null,
                "HasLike": true,
                "MetastoreType": "HIVE",
                "DatabaseName": "database-name",
                "StorageSize": 0,
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "TableOwnerId": "owner-id",
                "OwnerProjectId": "project-id"
            }
        ],
        "TotalCount": 10,
        "RequestId": "91300e24-4685-4f08-8870-b46ad2fad146"
    }
}
```

