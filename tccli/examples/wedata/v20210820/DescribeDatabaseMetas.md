**Example 1: 请求demo**



Input: 

```
tccli wedata DescribeDatabaseMetas --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 9999 \
    --Filters.0.Name datasourceId \
    --Filters.0.Values 146721 \
    --OrderFields.0.Name databaseName \
    --OrderFields.0.Direction ASC
```

Output: 
```
{
    "Response": {
        "RequestId": "e4037646-f140-4b15-bc22-aec12e2e1d70",
        "DatabaseMeta": [
            {
                "DatabaseId": null,
                "DatabaseGuid": null,
                "DatabaseName": "atta_boss",
                "ProjectId": "project_id_***",
                "ProjectName": "project_eng_name",
                "ProjectDisplayName": "项目中文名称",
                "MetastoreType": "DLC",
                "DatasourceId": 146721,
                "DatasourceName": "dlc_***",
                "DisplayName": "dlc_***.atta_boss",
                "Category": "CLUSTER",
                "Catalog": "DataLakeCatalog",
                "Description": "员工域数据",
                "Instance": "fkiqo0om",
                "OwnerAccount": 100000,
                "OwnerAccountName": "root",
                "Region": "ap-guangzhou",
                "Status": 1,
                "StorageSize": 536870912,
                "StorageSizeWithUnit": "512.00MB",
                "CreateTime": "2023-03-09 15:42:59",
                "TableCount": 12,
                "DatasourceList": [
                    {
                        "DatasourceId": "146721",
                        "DatasourceName": "dlc_***",
                        "DatasourceClusterId": "fkiqo0om",
                        "DatasourceUrn": "dlc_***",
                        "DatasourceEnv": "production"
                    }
                ],
                "CollectJobId": "collect_job_***",
                "CollectJobName": "dlc_采集任务",
                "ClusterId": "fkiqo0om",
                "ClusterName": "DLC实例-***",
                "OperateOption": null,
                "ModifiedTimeByTables": 1770625474000,
                "LastAccessTimeByTables": 1770625474000
            },
            {
                "DatabaseId": null,
                "DatabaseGuid": null,
                "DatabaseName": "atta_dw_base",
                "ProjectId": "project_id_***",
                "ProjectName": "project_eng_name",
                "ProjectDisplayName": "项目中文名称",
                "MetastoreType": "DLC",
                "DatasourceId": 146721,
                "DatasourceName": "dlc_***",
                "DisplayName": "dlc_***.atta_dw_base",
                "Category": "CLUSTER",
                "Catalog": "DataLakeCatalog",
                "Description": "ODS层：数据冷备",
                "Instance": "fkiqo0om",
                "OwnerAccount": 100000,
                "OwnerAccountName": "root",
                "Region": "ap-guangzhou",
                "Status": 1,
                "StorageSize": 268435456,
                "StorageSizeWithUnit": "256.00MB",
                "CreateTime": "2023-03-09 15:42:59",
                "TableCount": 8,
                "DatasourceList": [],
                "CollectJobId": null,
                "CollectJobName": null,
                "ClusterId": "fkiqo0om",
                "ClusterName": "DLC实例-***",
                "OperateOption": null,
                "ModifiedTimeByTables": null,
                "LastAccessTimeByTables": null
            }
        ]
    }
}
```

