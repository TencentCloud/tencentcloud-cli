**Example 1: 创建网络流日志**

创建网络流日志

Input: 

```
tccli vpc CreateFlowLog --cli-unfold-argument  \
    --FlowLogName demo \
    --CloudLogId dfb8f1a2-8522-47c1-8571-67905167ab3f \
    --VpcId vpc-pq9vxykj \
    --FlowLogDescription demo \
    --ResourceType NETWORKINTERFACE \
    --ResourceId eni-78ysaex1 \
    --TrafficType ACCEPT
```

Output: 
```
{
    "Response": {
        "FlowLog": [
            {
                "VpcId": "vpc-pq9vxykj",
                "FlowLogId": "fl-f42uhpkj",
                "FlowLogName": "demo",
                "ResourceType": "NETWORKINTERFACE",
                "ResourceId": "eni-78ysaex1",
                "TrafficType": "ACCEPT",
                "CloudLogId": "dfb8f1a2-8522-47c1-8571-67905167ab3f",
                "CloudLogState": "",
                "CloudLogRegion": "",
                "FlowLogDescription": "",
                "Enable": true,
                "StorageType": "cls",
                "TagSet": [
                    {
                        "Key": "city",
                        "Value": "shanghai"
                    }
                ],
                "FlowLogStorage": {
                    "StorageTopic": "",
                    "StorageId": ""
                },
                "CreatedTime": "0000-00-00 00:00:00"
            }
        ],
        "RequestId": "404428db-f850-40c2-803"
    }
}
```

