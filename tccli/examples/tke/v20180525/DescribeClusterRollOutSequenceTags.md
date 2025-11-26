**Example 1: 获取集群发布序列标签**

获取集群发布序列标签

Input: 

```
tccli tke DescribeClusterRollOutSequenceTags --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "f1048559-c7e4-4a7b-9d12-bc0256be3e26",
        "TotalCount": 1,
        "ClusterTags": [
            {
                "ClusterID": "cls-12345678",
                "Region": "ap-guangzhou",
                "Tags": [
                    "Test"
                ]
            }
        ]
    }
}
```

