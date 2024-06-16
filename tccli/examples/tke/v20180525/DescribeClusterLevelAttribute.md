**Example 1: 获取托管集群规模**



Input: 

```
tccli tke DescribeClusterLevelAttribute --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "7f654d68-0f64-4195-8aa8-5351bc441402",
        "Items": [
            {
                "Name": "L5",
                "Alias": "500节点",
                "NodeCount": 500,
                "PodCount": 1000,
                "ConfigMapCount": 200,
                "CRDCount": 1,
                "OtherCount": 1,
                "RSCount": 1,
                "Enable": true
            }
        ]
    }
}
```

