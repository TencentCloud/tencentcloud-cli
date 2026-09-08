**Example 1: 查询资源图谱详情**



Input: 

```
tccli cls DescribeResourceGraphDetail --cli-unfold-argument  \
    --ResourceGraphId 92005fca-cbf5-45e9-8c55-a506d8ff7238
```

Output: 
```
{
    "Response": {
        "ResourceGraphDetailInfo": {
            "AccessCount": 1,
            "CreateTime": 1784256669,
            "Name": "graph-name",
            "Products": [
                "tke"
            ],
            "RelationLogset": {
                "LogsetId": "977bfbf8-aeed-4932-8b05-e757301dcd7c",
                "LogsetName": "graph-logset-92005fca-cbf5-45e9-8c55-a506d8ff7238"
            },
            "RelationTopics": [
                {
                    "TopicId": "d2800f1b-cb58-415b-b53a-99a130d6b462",
                    "TopicName": "graph-entity-log-topic",
                    "Type": "entity"
                }
            ],
            "ResourceGraphId": "92005fca-cbf5-45e9-8c55-a506d8ff7238",
            "Status": 1,
            "Tags": [],
            "UpdateTime": 1785316923
        },
        "RequestId": "bbb6aedd-a7d0-4372-aff6-32fa6ca3ce07"
    }
}
```

