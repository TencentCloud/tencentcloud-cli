**Example 1: 查询流日志实例信息**

查询流日志实例信息

Input: 

```
tccli vpc DescribeFlowLog --cli-unfold-argument  \
    --VpcId vpc-pq9vxykj \
    --FlowLogId fl-f42uhpkj
```

Output: 
```
{
    "Response": {
        "FlowLog": [
            {
                "CloudLogId": "dfb8f1a2-8522-47c1-8571-67905167ab3f",
                "CloudLogState": "SUCCESS",
                "CreatedTime": "2019-05-08 10:48:26",
                "FlowLogDescription": "",
                "FlowLogId": "fl-f42uhpkj",
                "FlowLogName": "test",
                "ResourceId": "eni-78ysaex1",
                "ResourceType": "NETWORKINTERFACE",
                "TrafficType": "ACCEPT",
                "VpcId": "vpc-pq9vxykj",
                "StorageType": "cls",
                "FlowLogStorage": {
                    "StorageTopic": "topic-siqmaox1",
                    "StorageId": "ckafka-akwiqms1"
                },
                "TagSet": [],
                "Enable": true,
                "CloudLogRegion": ""
            }
        ],
        "RequestId": "404428db-f850-40c2-803d-0aae49aba43a"
    }
}
```

