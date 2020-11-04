**Example 1: 获取集群关联的标签列表**

获取集群关联的标签列表

Input: 

```
tccli tcaplusdb DescribeClusterTags --cli-unfold-argument  \
    --ClusterIds 5674209986
```

Output: 
```
{
    "Response": {
        "RequestId": "abd7111a-62d4-4bbb-a781-3646040e9530",
        "TotalCount": 1,
        "Rows": [
            {
                "ClusterId": "5674209986",
                "Tags": {
                    "TagKey": "test1",
                    "TagValue": "value1"
                }
            }
        ]
    }
}
```

