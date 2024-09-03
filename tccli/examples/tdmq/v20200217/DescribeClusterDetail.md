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
            "ClusterId": "abc",
            "ClusterName": "abc",
            "Remark": "abc",
            "EndPointNum": 0,
            "CreateTime": "abc",
            "Healthy": 0,
            "HealthyInfo": "abc",
            "Status": 0,
            "MaxNamespaceNum": 0,
            "MaxTopicNum": 0,
            "MaxQps": 0,
            "MessageRetentionTime": 0,
            "MaxStorageCapacity": 0,
            "Version": "abc",
            "PublicEndPoint": "abc",
            "VpcEndPoint": "abc",
            "NamespaceNum": 0,
            "UsedStorageBudget": 0,
            "MaxPublishRateInMessages": 0,
            "MaxDispatchRateInMessages": 0,
            "MaxPublishRateInBytes": 0,
            "MaxDispatchRateInBytes": 0,
            "TopicNum": 0,
            "MaxMessageDelayInSeconds": 0,
            "PublicAccessEnabled": true,
            "Tags": [
                {
                    "TagKey": "abc",
                    "TagValue": "abc"
                }
            ],
            "PayMode": 0,
            "ProjectId": 0,
            "ProjectName": "abc"
        },
        "RequestId": "abc"
    }
}
```

