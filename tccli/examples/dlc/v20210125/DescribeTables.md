**Example 1: 示例1**

查询数据表列表。

Input: 

```
tccli dlc DescribeTables --cli-unfold-argument  \
    --Limit 1 \
    --Offset 0 \
    --DatabaseName testdb \
    --DatasourceConnectionName DataLakeCatalog
```

Output: 
```
{
    "Response": {
        "TableList": [
            {
                "TableBaseInfo": {
                    "DatabaseName": "abc",
                    "TableName": "abc",
                    "DatasourceConnectionName": "abc",
                    "TableComment": "abc",
                    "Type": "abc",
                    "TableFormat": "abc",
                    "UserAlias": "abc",
                    "UserSubUin": "abc",
                    "GovernPolicy": {
                        "RuleType": "abc",
                        "GovernEngine": "abc"
                    },
                    "DbGovernPolicyIsDisable": "abc",
                    "SmartPolicy": {
                        "BaseInfo": {
                            "Uin": "abc",
                            "PolicyType": "abc",
                            "Catalog": "abc",
                            "Database": "abc",
                            "Table": "abc",
                            "AppId": "abc"
                        },
                        "Policy": {
                            "Inherit": "abc",
                            "Resources": [
                                {
                                    "AttributionType": "abc",
                                    "ResourceType": "abc",
                                    "Name": "abc",
                                    "Instance": "abc",
                                    "Favor": [
                                        {
                                            "Priority": 0,
                                            "Catalog": "abc",
                                            "DataBase": "abc",
                                            "Table": "abc"
                                        }
                                    ],
                                    "Status": 0
                                }
                            ],
                            "Written": {},
                            "Lifecycle": {
                                "LifecycleEnable": "abc",
                                "Expiration": 0,
                                "DropTable": true
                            },
                            "Index": {
                                "IndexEnable": "abc"
                            }
                        }
                    }
                },
                "Columns": [
                    {
                        "Name": "abc",
                        "Type": "abc",
                        "Comment": "abc",
                        "Precision": 0,
                        "Scale": 0,
                        "Nullable": "abc",
                        "Position": 0,
                        "CreateTime": "abc",
                        "ModifiedTime": "abc",
                        "IsPartition": true
                    }
                ],
                "Partitions": [
                    {
                        "Name": "abc",
                        "Type": "abc",
                        "Comment": "abc",
                        "Transform": "abc",
                        "TransformArgs": [
                            "abc"
                        ],
                        "CreateTime": 0
                    }
                ],
                "Location": "abc",
                "Properties": [
                    {
                        "Key": "abc",
                        "Value": "abc"
                    }
                ],
                "ModifiedTime": "abc",
                "CreateTime": "abc",
                "InputFormat": "abc",
                "StorageSize": 0,
                "RecordCount": 0,
                "MapMaterializedViewName": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

