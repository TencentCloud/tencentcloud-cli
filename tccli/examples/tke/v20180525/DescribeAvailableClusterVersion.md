**Example 1: 获取集群可以升级的版本**



Input: 

```
tccli tke DescribeAvailableClusterVersion --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "Clusters": [
            {
                "ClusterId": "xx",
                "Versions": [
                    "xx"
                ]
            }
        ],
        "RequestId": "xx",
        "Versions": [
            "1.8.13"
        ]
    }
}
```

