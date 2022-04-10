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
                "MaxQps": 10000,
                "HealthyInfo": "xx",
                "MaxTopicNum": 1000,
                "MaxStorageCapacity": 100,
                "MaxMessageDelayInSeconds": 0,
                "Version": "xx",
                "Status": 1,
                "Tags": [
                    {
                        "TagKey": "xx",
                        "TagValue": "xx"
                    }
                ],
                "ClusterId": "xx",
                "PayMode": 0,
                "EndPointNum": 0,
                "Healthy": 1,
                "TopicNum": 0,
                "Remark": "xx",
                "NamespaceNum": 0,
                "PublicEndPoint": "xx",
                "MaxPublishRateInBytes": 0,
                "VpcEndPoint": "xx",
                "MaxDispatchRateInBytes": 0,
                "PublicAccessEnabled": true,
                "ClusterName": "xx",
                "MaxPublishRateInMessages": 0,
                "UsedStorageBudget": 0,
                "MessageRetentionTime": 86400,
                "MaxNamespaceNum": 10,
                "CreateTime": "xx",
                "MaxDispatchRateInMessages": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

