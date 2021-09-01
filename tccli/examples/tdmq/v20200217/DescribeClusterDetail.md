**Example 1: 获取集群的详细信息**



Input: 

```
tccli tdmq DescribeClusterDetail --cli-unfold-argument  \
    --ClusterId pulsar-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "ClusterSet": {
            "ClusterId": "pulsar-xxxxxxxx",
            "ClusterName": "sdfsdfsdf",
            "Remark": "",
            "EndPointNum": 0,
            "CreateTime": "2021-01-13 15:43:29",
            "Healthy": 1,
            "HealthyInfo": "",
            "Status": 1,
            "MaxNamespaceNum": 50,
            "MaxTopicNum": 1000,
            "MaxQps": 10000,
            "MessageRetentionTime": 86400,
            "VpcEndPoint": "xx",
            "NamespaceNum": 0,
            "Version": "xx",
            "PublicEndPoint": "xx",
            "MaxStorageCapacity": 100
        },
        "RequestId": "020eb354-144e-4cf8-9607-c6771cd24421"
    }
}
```

