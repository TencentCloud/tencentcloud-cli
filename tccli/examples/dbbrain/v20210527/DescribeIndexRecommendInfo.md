**Example 1: mongodb索引推荐**

查询mongodb数据比较慢的时候，可以通过该接口进行获取推荐的索引列表

Input: 

```
tccli dbbrain DescribeIndexRecommendInfo --cli-unfold-argument  \
    --Product mongodb \
    --InstanceId cmog-ahshjbdwe
```

Output: 
```
{
    "Response": {
        "CollectionNum": 0,
        "IndexNum": 0,
        "Items": [
            {
                "ClusterId": "abc",
                "Collection": "abc",
                "Db": "abc",
                "Level": 0,
                "Score": 0,
                "IndexesToBuild": [
                    {
                        "Id": 0,
                        "IndexCommand": "abc",
                        "IndexStr": "abc",
                        "Level": 0,
                        "Score": 0,
                        "Signs": [
                            "abc"
                        ],
                        "Status": 0
                    }
                ],
                "IndexesToDrop": [
                    {
                        "IndexStr": "abc",
                        "Score": 0,
                        "Reason": "abc",
                        "IndexCommand": "abc",
                        "IndexName": "abc"
                    }
                ]
            }
        ],
        "Level": 0,
        "Optimized": 0,
        "OptimizedCount": 0,
        "RequestId": "abc"
    }
}
```

