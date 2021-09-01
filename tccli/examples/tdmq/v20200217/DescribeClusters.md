**Example 1: 获取集群列表**



Input: 

```
tccli tdmq DescribeClusters --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ClusterSet": [
            {
                "ClusterId": "pulsar-p37angkrqd",
                "ClusterName": "default",
                "Remark": "default",
                "EndPointNum": 0,
                "CreateTime": "2020-11-30 20:45:36",
                "Healthy": 1,
                "HealthyInfo": "",
                "Status": 1,
                "MaxNamespaceNum": 10,
                "MaxTopicNum": 1000,
                "MaxQps": 10000,
                "MessageRetentionTime": 86400,
                "NamespaceNum": 0,
                "VpcEndPoint": "xx",
                "PublicEndPoint": "xx",
                "Version": "xx",
                "MaxStorageCapacity": 100
            }
        ],
        "RequestId": "137c3d2c-eae6-4545-95dd-0d332074fd0e"
    }
}
```

