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
        "Rows": [
            {
                "ClusterId": "abc",
                "Tags": [
                    {
                        "TagKey": "abc",
                        "TagValue": "abc"
                    }
                ],
                "Error": {
                    "Code": "abc",
                    "Message": "abc"
                }
            }
        ],
        "TotalCount": 0,
        "RequestId": "abc"
    }
}
```

