**Example 1: shili1**



Input: 

```
tccli wedata CreateLogicTable --cli-unfold-argument  \
    --TaskId asdfas \
    --DatasourceType asdfasdf \
    --DatasourceIds adsf \
    --ShardingDatasourceInfos.0.RuleId asdf \
    --ShardingDatasourceInfos.0.LogicDatabase asdf \
    --ShardingDatasourceInfos.0.LogicSchema asdf \
    --ShardingDatasourceInfos.0.LogicTable asdf \
    --ShardingDatasourceInfos.0.SourceDatabase asdf \
    --ShardingDatasourceInfos.0.SourceSchema asdf \
    --ShardingDatasourceInfos.0.SourceTable asdf \
    --WorkspaceId asdf \
    --Model asdf
```

Output: 
```
{
    "Response": {
        "Data": {
            "LogicTableResults": [
                {
                    "DataStructs": [
                        {
                            "DatabaseStructs": [
                                {
                                    "DatabaseName": "43",
                                    "SchemaStructs": [],
                                    "Tables": []
                                }
                            ],
                            "DatasourceId": "12312",
                            "Instance": "1"
                        }
                    ],
                    "LogicDatabase": "3",
                    "LogicSchema": "4",
                    "LogicTable": "5",
                    "RuleId": "2",
                    "UniKey": "1"
                }
            ]
        },
        "RequestId": "81e31486-c714-475a-9300-7de74e42e97a"
    }
}
```

