**Example 1: 查询数据源元数据**



Input: 

```
tccli wedata DescribeDatabaseMeta --cli-unfold-argument  \
    --DatabaseId guid_of_database_***
```

Output: 
```
{
    "Response": {
        "RequestId": "req_id_***",
        "DatabaseMeta": {
            "DatabaseId": null,
            "DatabaseGuid": "guid_of_database_***",
            "DatabaseName": "example_db",
            "ProjectId": "project_id_***",
            "ProjectName": "project_eng_name",
            "ProjectDisplayName": "项目中文名称",
            "MetastoreType": "HIVE",
            "DatasourceId": 79541,
            "DatasourceName": "hive_emr-***",
            "DisplayName": "hive_emr-***.example_db",
            "Category": "CLUSTER",
            "Catalog": "hive",
            "Description": "业务数据库",
            "Instance": "emr-***",
            "OwnerAccount": 100000,
            "OwnerAccountName": "hadoop",
            "Region": "ap-guangzhou",
            "Status": 1,
            "StorageSize": 1073741824,
            "StorageSizeWithUnit": "1.00GB",
            "CreateTime": "2023-03-09 15:42:59",
            "TableCount": 56,
            "DatasourceList": [
                {
                    "DatasourceId": "79541",
                    "DatasourceName": "hive_emr-***",
                    "DatasourceClusterId": "emr-***",
                    "DatasourceUrn": "hive_emr-***",
                    "DatasourceEnv": "production"
                }
            ],
            "CollectJobId": "collect_job_***",
            "CollectJobName": "hive_采集任务",
            "ClusterId": "emr-***",
            "ClusterName": "EMR-***集群",
            "OperateOption": null,
            "ModifiedTimeByTables": 1770625474000,
            "LastAccessTimeByTables": 1770625474000
        }
    }
}
```

