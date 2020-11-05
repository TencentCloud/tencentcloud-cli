**Example 1: Obtaining the list of tags associated with a cluster**

This example shows you how to obtain the list of tags associated with a cluster.

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

