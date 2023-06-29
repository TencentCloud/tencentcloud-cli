**Example 1: 示例**



Input: 

```
tccli cdwch DescribeInstanceClusters --cli-unfold-argument  \
    --InstanceId xx
```

Output: 
```
{
    "Response": {
        "Clusters": [
            {
                "ClusterName": "xx",
                "NodeIps": [
                    "xx"
                ]
            }
        ],
        "RequestId": "xx"
    }
}
```

