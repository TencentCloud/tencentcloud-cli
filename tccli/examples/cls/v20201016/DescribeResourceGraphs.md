**Example 1: 查询资源图谱列表**



Input: 

```
tccli cls DescribeResourceGraphs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ResourceGraphInfos": [
            {
                "CreateTime": 1784269960,
                "Name": "test-yangxyang11",
                "RelationLogset": {
                    "LogsetId": "ff768190-a5b0-48d1-8a5a-78f148a56422",
                    "LogsetName": "graph-logset-34b7ad8b-fb4c-42de-a7e1-2442202bad02"
                },
                "RelationTopics": [
                    {
                        "TopicId": "d4cf2dd5-3e50-43df-b21a-98406b509d87",
                        "TopicName": "graph-entity-log-topic",
                        "Type": "entity"
                    }
                ],
                "ResourceGraphId": "34b7ad8b-fb4c-42de-a7e1-2442202bad02",
                "Status": 1,
                "Tags": [],
                "UpdateTime": 1784269965
            }
        ],
        "TotalCount": 20,
        "RequestId": "d3251d25-b5fd-4c08-b13a-c6eea8fdd6f3"
    }
}
```

