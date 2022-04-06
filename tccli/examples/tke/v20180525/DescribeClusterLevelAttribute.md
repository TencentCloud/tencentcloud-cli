**Example 1: 获取托管集群规模**



Input: 

```
tccli tke DescribeClusterLevelAttribute --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "Items": [
            {
                "Name": "L5",
                "Alias": "500节点",
                "NodeCount": 500,
                "PodCount": 1000,
                "ConfigMapCount": 200,
                "CRDCount": 1,
                "OtherCount": 1,
                "Enable": true
            }
        ]
    }
}
```

