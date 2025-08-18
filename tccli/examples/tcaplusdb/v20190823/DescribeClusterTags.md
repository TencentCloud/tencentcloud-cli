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
                "ClusterId": "19887328",
                "Tags": [
                    {
                        "TagKey": "tkey1",
                        "TagValue": "tvalue1"
                    }
                ],
                "Error": {
                    "Code": "",
                    "Message": ""
                }
            }
        ],
        "TotalCount": 0,
        "RequestId": "189382-121421"
    }
}
```

