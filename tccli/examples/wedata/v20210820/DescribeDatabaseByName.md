**Example 1: 根据数据库名称查询数据库信息**

根据数据库名称查询数据库信息

Input: 

```
tccli wedata DescribeDatabaseByName --cli-unfold-argument  \
    --DatabaseName atta_boss \
    --DatasourceId 146721 \
    --SchemaName None \
    --ClusterId None
```

Output: 
```
{
    "Response": {
        "RequestId": "req_id_***",
        "DatabaseMeta": {
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
            "OwnerAccount": 100000123456,
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
        }
    }
}
```

