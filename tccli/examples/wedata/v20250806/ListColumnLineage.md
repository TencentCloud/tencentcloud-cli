**Example 1: 查询字段血缘**



Input: 

```
tccli wedata ListColumnLineage --cli-unfold-argument  \
    --TableUniqueId b4JSso6coG4BU96R-jkQEg
 \
    --Direction OUTPUT \
    --PageNumber 1 \
    --PageSize 10 \
    --ColumnName id \
    --Platform WEDATA
```

Output: 
```
{
    "Response": {
        "RequestId": "req_id_***",
        "Data": {
            "PageCount": 1,
            "PageSize": 20,
            "PageNumber": 1,
            "TotalCount": 2,
            "Items": [
                {
                    "Resource": {
                        "ResourceUniqueId": "guid_of_table::item_nbr",
                        "ResourceName": "item_nbr",
                        "ResourceType": "COLUMN",
                        "LineageNodeId": "wedata::COLUMN::100000123456::guid_of_table::item_nbr",
                        "Description": "商品编号",
                        "Platform": "WEDATA",
                        "CreateTime": "2025-06-01 10:00:00",
                        "UpdateTime": "2025-06-15 14:30:00",
                        "ResourceProperties": [
                            {
                                "Name": "DatabaseName",
                                "Value": "dwd_db"
                            },
                            {
                                "Name": "CatalogName",
                                "Value": "DataLakeCatalog"
                            },
                            {
                                "Name": "SchemaName",
                                "Value": ""
                            },
                            {
                                "Name": "TableName",
                                "Value": "DataLakeCatalog.dwd_db.dwd_example_table"
                            },
                            {
                                "Name": "TableType",
                                "Value": "MANAGED_TABLE"
                            },
                            {
                                "Name": "Description",
                                "Value": "商品编号"
                            },
                            {
                                "Name": "ColumnType",
                                "Value": "bigint"
                            },
                            {
                                "Name": "ColumnName",
                                "Value": "item_nbr"
                            },
                            {
                                "Name": "TableId",
                                "Value": "guid_of_table"
                            }
                        ]
                    },
                    "Relation": {
                        "RelationId": "wedata::COLUMN::100000123456::guid_of_table::item_nbr::wedata::COLUMN::100000123456::guid_downstream_1::product_id",
                        "SourceUniqueId": "wedata::COLUMN::100000123456::guid_of_table::item_nbr",
                        "TargetUniqueId": "wedata::COLUMN::100000123456::guid_downstream_1::product_id",
                        "Processes": [
                            {
                                "ProcessId": "task_67890",
                                "ProcessType": "WEDATA_TASK",
                                "ProcessSubType": "SQL_TASK",
                                "LineageNodeId": "wedata::PROCESS::100000123456::task_67890",
                                "Platform": "WEDATA",
                                "ProcessProperties": []
                            }
                        ]
                    },
                    "DownStreamCount": 1,
                    "UpStreamCount": 0
                }
            ]
        }
    }
}
```

