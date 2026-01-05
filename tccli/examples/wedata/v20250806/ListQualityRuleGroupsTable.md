**Example 1: 查询规则组关联表信息**

查询规则组关联表信息

Input: 

```
tccli wedata ListQualityRuleGroupsTable --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --ProjectId 1464962169590902784
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CatalogName": null,
                    "CreateTime": "2025-11-26 12:06:32",
                    "DatabaseName": "default",
                    "DatasourceId": "61949",
                    "DatasourceName": "tchouse-x_instance-h3r2r46y",
                    "EnableRuleGroupCount": 1,
                    "Id": 353,
                    "InstanceId": null,
                    "RuleCount": 2,
                    "RuleGroupCount": 1,
                    "SchemaName": null,
                    "TableName": "bbb",
                    "TableOwnerName": null,
                    "TableOwnerUserId": null,
                    "UpdateTime": "2025-11-26 12:06:32"
                },
                {
                    "CatalogName": null,
                    "CreateTime": "2025-11-25 14:21:39",
                    "DatabaseName": "awq",
                    "DatasourceId": "8549",
                    "DatasourceName": "dlc_u54usqbq",
                    "EnableRuleGroupCount": 1,
                    "Id": 352,
                    "InstanceId": null,
                    "RuleCount": 1,
                    "RuleGroupCount": 1,
                    "SchemaName": null,
                    "TableName": "test_fq",
                    "TableOwnerName": null,
                    "TableOwnerUserId": null,
                    "UpdateTime": "2025-11-25 16:03:15"
                },
                {
                    "CatalogName": null,
                    "CreateTime": "2025-05-14 17:09:42",
                    "DatabaseName": "default",
                    "DatasourceId": "61557",
                    "DatasourceName": "hive_emr-onelrijj",
                    "EnableRuleGroupCount": 1,
                    "Id": 345,
                    "InstanceId": null,
                    "RuleCount": 1,
                    "RuleGroupCount": 1,
                    "SchemaName": null,
                    "TableName": "employee",
                    "TableOwnerName": null,
                    "TableOwnerUserId": null,
                    "UpdateTime": "2025-05-14 17:09:42"
                }
            ],
            "TotalCount": 3
        },
        "RequestId": "0f99dbd2-5ef7-4d90-a9ac-cef9eae0d1b7"
    }
}
```

**Example 2: 查询项目的某个数据源下已创建规则组（监控）的表信息**



Input: 

```
tccli wedata ListQualityRuleGroupsTable --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --PageNumber 1 \
    --PageSize 10 \
    --Filters.0.Name DatasourceType \
    --Filters.0.Values 3 \
    --Filters.1.Name DatasourceId \
    --Filters.1.Values 8860 \
    --Filters.2.Name DatabaseName \
    --Filters.3.Name SchemaName
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CatalogName": "DataLakeCatalog",
                    "CreateTime": "2025-01-21 16:21:29",
                    "DatabaseName": "at_dlc_cloud_gz_prod_mc",
                    "DatasourceId": "8860",
                    "DatasourceName": "dlc_DLC_hx756s1y",
                    "EnableRuleGroupCount": 1,
                    "Id": 328,
                    "InstanceId": null,
                    "RuleCount": 9,
                    "RuleGroupCount": 1,
                    "SchemaName": null,
                    "TableName": "gee01",
                    "TableOwnerName": null,
                    "TableOwnerUserId": null,
                    "UpdateTime": "2025-12-30 20:26:57"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "ac8ee1e0-3ff7-47dc-aa1d-59affc93de8f"
    }
}
```

