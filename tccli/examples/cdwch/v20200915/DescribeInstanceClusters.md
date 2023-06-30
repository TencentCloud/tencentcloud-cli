**Example 1: 示例**

查询cluster列表

Input: 

```
tccli cdwch DescribeInstanceClusters --cli-unfold-argument  \
    --InstanceId cdwch-asdf8max
```

Output: 
```
{
    "Response": {
        "Clusters": [
            {
                "ClusterName": "default_cluster",
                "NodeIps": [
                    "10.2.23.43"
                ]
            }
        ],
        "RequestId": "asdfa-xa1dads-8amsad"
    }
}
```

