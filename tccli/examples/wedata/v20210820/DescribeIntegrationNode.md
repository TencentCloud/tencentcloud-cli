**Example 1: DescribeIntegrationNode**

查询集成节点

Input: 

```
tccli wedata DescribeIntegrationNode --cli-unfold-argument  \
    --Id 14342 \
    --ProjectId 11022568003970304 \
    --TaskType 201
```

Output: 
```
{
    "Response": {
        "NodeInfo": {
            "Id": "1",
            "TaskId": "20220331184313320",
            "Name": "1",
            "NodeType": "INPUT",
            "DataSourceType": "MYSQL",
            "Description": "NULL",
            "DatasourceId": "72036",
            "Config": [
                {
                    "Name": "isClean",
                    "Value": "0"
                },
                {
                    "Name": "fieldDelimiter",
                    "Value": ","
                },
                {
                    "Name": "encoding",
                    "Value": "utf-8"
                },
                {
                    "Name": "Database",
                    "Value": "auto_test_db"
                },
                {
                    "Name": "TableNames",
                    "Value": "auto_mysql_table_1"
                },
                {
                    "Name": "SiblingNodes",
                    "Value": "[]"
                }
            ],
            "ExtConfig": [
                {
                    "Name": "x",
                    "Value": "280"
                },
                {
                    "Name": "y",
                    "Value": "150"
                },
                {
                    "Name": "iconPosition",
                    "Value": "left"
                },
                {
                    "Name": "size",
                    "Value": "m"
                },
                {
                    "Name": "imgHref",
                    "Value": "https://imgcache.qq.com/qcloud/tcloud_dtc/static/We_Data/72b24f22-a090-4052-9452-b0b9f38565e3.svg"
                },
                {
                    "Name": "disType",
                    "Value": "MySQL"
                }
            ],
            "Schema": [
                {
                    "Id": "517902752",
                    "Name": "col1",
                    "Value": null,
                    "Type": "int(11)",
                    "Properties": [
                        {
                            "Name": "12231",
                            "Value": "ab23123c"
                        }
                    ],
                    "Alias": "1111",
                    "Comment": "1111"
                }
            ],
            "NodeMapping": {
                "SourceId": "3041",
                "SinkId": "3042",
                "SourceSchema": null,
                "ExtConfig": [
                    {
                        "Name": "fromNode",
                        "Value": "node_3041"
                    },
                    {
                        "Name": "toNode",
                        "Value": "node_3042"
                    },
                    {
                        "Name": "fromNodeAnchor",
                        "Value": "bottom"
                    },
                    {
                        "Name": "toNodeAnchor",
                        "Value": "top"
                    }
                ],
                "SchemaMappings": null
            },
            "AppId": "1257305158",
            "ProjectId": "1",
            "CreatorUin": "100022744352",
            "OperatorUin": "100022744352",
            "OwnerUin": "100006908545",
            "CreateTime": "2022-03-31 18:43:24",
            "UpdateTime": "2023-03-31 18:43:24"
        },
        "SourceCheckFlag": true,
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

