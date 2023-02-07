**Example 1: 示例一**



Input: 

```
tccli region DescribeCluster --cli-unfold-argument  \
    --Zone xx
```

Output: 
```
{
    "Response": {
        "ResourceClusterSet": [
            {
                "ClusterName": "xx",
                "Priority": 0,
                "ClusterId": 0,
                "Zone": "xx",
                "ZoneName": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

