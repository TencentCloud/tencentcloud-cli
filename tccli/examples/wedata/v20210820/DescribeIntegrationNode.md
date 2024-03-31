**Example 1: DescribeIntegrationNode**

查询集成节点

Input: 

```
tccli wedata DescribeIntegrationNode --cli-unfold-argument  \
    --Id abc \
    --ProjectId abc \
    --TaskType 1
```

Output: 
```
{
    "Response": {
        "NodeInfo": {
            "Id": "abc",
            "TaskId": "abc",
            "Name": "abc",
            "NodeType": "abc",
            "DataSourceType": "abc",
            "Description": "abc",
            "DatasourceId": "abc",
            "Config": [
                {
                    "Name": "abc",
                    "Value": "abc"
                }
            ],
            "ExtConfig": [
                {
                    "Name": "abc",
                    "Value": "abc"
                }
            ],
            "Schema": [
                {
                    "Id": "abc",
                    "Name": "abc",
                    "Value": "abc",
                    "Type": "abc",
                    "Properties": [
                        {
                            "Name": "abc",
                            "Value": "abc"
                        }
                    ],
                    "Alias": "abc",
                    "Comment": "abc"
                }
            ],
            "NodeMapping": {
                "SourceId": "abc",
                "SinkId": "abc",
                "SourceSchema": [
                    {
                        "Id": "abc",
                        "Name": "abc",
                        "Value": "abc",
                        "Type": "abc",
                        "Alias": "abc",
                        "Properties": [
                            {
                                "Name": "abc",
                                "Value": "abc"
                            }
                        ],
                        "Comment": "abc"
                    }
                ],
                "SchemaMappings": [
                    {
                        "SourceSchemaId": "abc",
                        "SinkSchemaId": "abc"
                    }
                ]
            },
            "AppId": "abc",
            "ProjectId": "abc",
            "CreatorUin": "abc",
            "OperatorUin": "abc",
            "OwnerUin": "abc",
            "CreateTime": "abc",
            "UpdateTime": "abc"
        },
        "SourceCheckFlag": true,
        "RequestId": "abc"
    }
}
```

