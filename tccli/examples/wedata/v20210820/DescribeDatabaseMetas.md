**Example 1: 请求demo**



Input: 

```
tccli wedata DescribeDatabaseMetas --cli-unfold-argument  \
    --Filters.0.Name a1 \
    --Filters.0.Values 1 \
    --OrderFields.0.Name a1b1c \
    --OrderFields.0.Direction a1b1c \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "DatabaseMeta": [
            {
                "Catalog": null,
                "Category": null,
                "ClusterId": null,
                "ClusterName": null,
                "CollectJobId": null,
                "CollectJobName": null,
                "CreateTime": "2025-08-12T16:00:53+08:00",
                "DatabaseGuid": "FB-gjv53p2TZcPaaZmsGHw",
                "DatabaseId": "31712",
                "DatabaseName": "barry_4",
                "DatasourceId": 93731,
                "DatasourceList": null,
                "DatasourceName": "hive_emr-3f0wn6y7",
                "Description": null,
                "DisplayName": "hive_emr-3f0wn6y7.barry_4",
                "Environment": null,
                "Instance": null,
                "LastAccessTimeByTables": null,
                "MetastoreType": "HIVE",
                "ModifiedTimeByTables": null,
                "OwnerAccountName": null,
                "ProjectDisplayName": null,
                "ProjectId": null,
                "ProjectName": null,
                "Region": null,
                "Status": null,
                "StorageSize": null,
                "StorageSizeWithUnit": null,
                "TableCount": null
            }
        ],
        "RequestId": "d271201e-984c-439c-9672-142817b5414d"
    }
}
```

