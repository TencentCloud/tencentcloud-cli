**Example 1: mongodb索引推荐**

查询mongodb数据比较慢的时候，可以通过该接口进行获取推荐的索引列表

Input: 

```
tccli dbbrain DescribeIndexRecommendInfo --cli-unfold-argument  \
    --Product mongodb \
    --InstanceId cmgo-2jrxxlx
```

Output: 
```
{
    "Response": {
        "CollectionNum": 2,
        "IndexNum": 2,
        "Items": [
            {
                "ClusterId": "cmgo-2jrxxlx",
                "Collection": "t_socket_resource",
                "Db": "proxyx",
                "Level": 0,
                "Score": 0,
                "IndexesToBuild": [
                    {
                        "Id": 3626848,
                        "IndexCommand": "db.t_socket_resource.createIndex({ status: 1, expireTimestamp: 1 }, { background: true })",
                        "IndexStr": "{ status: 1, expireTimestamp: 1 }",
                        "Level": 4,
                        "Score": 20,
                        "Signs": [
                            "1a59c167379c9bb7b799b3fe1db95fe2"
                        ],
                        "Status": 0
                    }
                ],
                "IndexesToDrop": [
                    {
                        "IndexStr": "{ userId: 1, from: 1, action: 1 }",
                        "Score": 15,
                        "Reason": "与索引 { userId: 1, from: 1, action: 1, createdAt: -1 } 重复",
                        "IndexCommand": "db.editrecords.dropIndex(\"userId_1_from_1_action_1\")",
                        "IndexName": "userId_1_from_1_action_1"
                    }
                ]
            }
        ],
        "Level": 4,
        "Optimized": 0,
        "OptimizedCount": 0,
        "RequestId": "17fa8e11-c19c-11ef-82da-5f2abf40a8f2"
    }
}
```

