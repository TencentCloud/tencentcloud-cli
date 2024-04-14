**Example 1: 查询集成任务版本节点信息**

查询集成任务版本节点信息

Input: 

```
tccli wedata DescribeIntegrationVersionNodesInfo --cli-unfold-argument  \
    --TaskId ap-|cos-|file.dg \
    --ProjectId 123 \
    --TaskVersionPath YXAtfGNvcy18ZmlsZV94eC5kZw== \
    --TaskVersion 202310060503283
```

Output: 
```
{
    "Response": {
        "Nodes": [
            {
                "Id": "130973",
                "TaskId": "n11a6d01c-0ec6-4efc-bd14-97a921d01d3f",
                "Name": "nodeTestName",
                "NodeType": "INPUT",
                "DataSourceType": "MYSQL",
                "Description": "testdesc",
                "DatasourceId": "914840",
                "Config": [
                    {
                        "Name": "Type",
                        "Value": "MYSQL"
                    },
                    {
                        "Name": "splitPk",
                        "Value": "id"
                    },
                    {
                        "Name": "Database",
                        "Value": "databasetestname"
                    },
                    {
                        "Name": "TableNames",
                        "Value": "tabletestname"
                    },
                    {
                        "Name": "PrimaryKey",
                        "Value": "id"
                    },
                    {
                        "Name": "isNew",
                        "Value": "true"
                    },
                    {
                        "Name": "PrimaryKey_INPUT_SYMBOL",
                        "Value": "input"
                    },
                    {
                        "Name": "splitPk_INPUT_SYMBOL",
                        "Value": "input"
                    },
                    {
                        "Name": "isClean",
                        "Value": "0"
                    },
                    {
                        "Name": "encoding",
                        "Value": "utf-8"
                    }
                ],
                "ExtConfig": [
                    {
                        "Name": "x",
                        "Value": "300"
                    },
                    {
                        "Name": "y",
                        "Value": "260"
                    },
                    {
                        "Name": "iconPosition",
                        "Value": "left"
                    },
                    {
                        "Name": "size",
                        "Value": "m"
                    }
                ],
                "Schema": [
                    {
                        "Type": "String",
                        "Alias": "name",
                        "Comment": "名字",
                        "Id": "616042880",
                        "Name": "name",
                        "Value": "nihao",
                        "Properties": [
                            {
                                "Name": "exttestname",
                                "Value": "exttestvalue"
                            }
                        ]
                    }
                ],
                "NodeMapping": {
                    "SourceId": "130973",
                    "SinkId": "130972",
                    "SourceSchema": [
                        {
                            "Id": "597853056",
                            "Name": "name",
                            "Value": "test",
                            "Type": "String",
                            "Alias": "name",
                            "Comment": "名称",
                            "Properties": [
                                {
                                    "Name": "exttestname",
                                    "Value": "exttestvalue"
                                }
                            ]
                        }
                    ],
                    "SchemaMappings": [
                        {
                            "SourceSchemaId": "597853056",
                            "SinkSchemaId": "616042880"
                        }
                    ],
                    "ExtConfig": [
                        {
                            "Name": "Type",
                            "Value": "MYSQL"
                        }
                    ]
                },
                "AppId": "1315051999",
                "ProjectId": "1486446569620893696",
                "CreatorUin": "100028644005",
                "OperatorUin": "100028644005",
                "OwnerUin": "100028644005",
                "CreateTime": "2022-05-07 10:13:21",
                "UpdateTime": "2022-05-07 10:13:21"
            }
        ],
        "Mappings": [
            {
                "SourceId": "130973",
                "SinkId": "130972",
                "SourceSchema": [
                    {
                        "Id": "597853056",
                        "Name": "name",
                        "Value": "test",
                        "Type": "String",
                        "Alias": "name",
                        "Comment": "名称",
                        "Properties": [
                            {
                                "Name": "exttestname",
                                "Value": "exttestvalue"
                            }
                        ]
                    }
                ],
                "SchemaMappings": [
                    {
                        "SourceSchemaId": "597853056",
                        "SinkSchemaId": "616042880"
                    }
                ],
                "ExtConfig": [
                    {
                        "Name": "ext key name",
                        "Value": "ext key value"
                    }
                ]
            }
        ],
        "TaskId": "n11a6d01c-0ec6-4efc-bd14-97a921d01d3f",
        "RequestId": "ae90b19-209e-4acb-9f62-e2860dd810"
    }
}
```

