**Example 1: 获取集群的详细信息**



Input: 

```
tccli tdmq DescribeClusterDetail --cli-unfold-argument  \
    --ClusterId pulsar-47emajuekabz
```

Output: 
```
{
    "Response": {
        "ClusterSet": {
            "ClusterId": "pulsar-47emajuekabz",
            "ClusterName": "devName",
            "Remark": "devRemark",
            "EndPointNum": 0,
            "HealthyInfo": "healthy",
            "CreateTime": "2023-07-20 10:35:17",
            "Healthy": 1,
            "Status": 0,
            "MaxNamespaceNum": 0,
            "MaxTopicNum": 0,
            "MaxQps": 0,
            "MessageRetentionTime": 0,
            "MaxStorageCapacity": 0,
            "Version": "2.9.2",
            "PublicEndPoint": null,
            "VpcEndPoint": null,
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
                    "TagKey": "pulsarTag",
                    "TagValue": "dev"
                }
            ],
            "PayMode": 0,
            "ProjectId": 0,
            "ProjectName": "dev"
        },
        "RequestId": "5d6c7091-e82c-4a9c-a18f-34d5fc460iuu"
    }
}
```

