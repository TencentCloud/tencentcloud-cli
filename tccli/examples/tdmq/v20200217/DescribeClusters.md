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
                "HealthyInfo": "ok",
                "MaxTopicNum": 1000,
                "MaxStorageCapacity": 100,
                "MaxMessageDelayInSeconds": 0,
                "Version": "v1",
                "Status": 1,
                "Tags": [
                    {
                        "TagKey": "tag1",
                        "TagValue": "value1"
                    }
                ],
                "ClusterId": "pulsar-xk3ne8k2qkp8",
                "PayMode": 0,
                "EndPointNum": 0,
                "Healthy": 1,
                "TopicNum": 0,
                "Remark": "beizhu",
                "NamespaceNum": 0,
                "PublicEndPoint": "http://mq.public.endpoint",
                "MaxPublishRateInBytes": 0,
                "VpcEndPoint": "http://mq.tencent.vpc.end.point",
                "MaxDispatchRateInBytes": 0,
                "PublicAccessEnabled": true,
                "ClusterName": "mq-cluster",
                "MaxPublishRateInMessages": 0,
                "UsedStorageBudget": 0,
                "MessageRetentionTime": 86400,
                "MaxNamespaceNum": 10,
                "CreateTime": "2024-10-08 11:38:48,068",
                "MaxDispatchRateInMessages": 0
            }
        ],
        "RequestId": "4446732a-8d0a-4549-9fb3-79949a788fc0"
    }
}
```

