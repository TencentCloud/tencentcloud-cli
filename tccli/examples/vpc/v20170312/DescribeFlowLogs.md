**Example 1: 查询流日志集合**

查询流日志集合

Input: 

```
tccli vpc DescribeFlowLogs --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "FlowLog": [
            {
                "CloudLogId": "dfb8f1a2-8522-47c1-8571-67905167ab3f",
                "CloudLogRegion": "ap-guangzhou",
                "CloudLogState": "SUCCESS",
                "CreatedTime": "2019-05-07 18:00:26",
                "FlowLogDescription": "",
                "FlowLogId": "fl-2edhcclz",
                "FlowLogName": "yuemingtest",
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
                "Enable": true
            },
            {
                "CloudLogId": "dfb8f1a2-8522-47c1-8571-67905167ab3f",
                "CloudLogRegion": "ap-guangzhou",
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
                "Enable": true
            }
        ],
        "TotalNum": 2,
        "RequestId": "404428db-f850-40c2-803d-0aae49aba43a"
    }
}
```

**Example 2: 获取流日志信息**

获取流日志信息

Input: 

```
tccli vpc DescribeFlowLogs --cli-unfold-argument  \
    --VpcId vpc-ew41hsdj \
    --FlowLogId fl-m4vogmhf
```

Output: 
```
{
    "Response": {
        "FlowLog": [
            {
                "VpcId": "vpc-ew41hsdj",
                "FlowLogId": "fl-m4vogmhf",
                "FlowLogName": "sflow-nat",
                "ResourceType": "NAT",
                "ResourceId": "nat-prlux840",
                "TrafficType": "ALL",
                "CloudLogId": "29a6c8c8-d57d-4e25-84b5-9114734ce6ca",
                "CloudLogRegion": "ap-guangzhou",
                "CloudLogState": "SUCCESS",
                "FlowLogDescription": "",
                "CreatedTime": "2022-05-18 15:26:50",
                "Enable": true,
                "StorageType": "cls",
                "FlowLogStorage": {
                    "StorageId": "29a6c8c8-d57d-4e25-84b5-9114734ce6ca"
                },
                "TagSet": []
            }
        ],
        "TotalNum": 1,
        "RequestId": "811bbd89-3c38-4926-9a8c-4bc97792aa34"
    }
}
```

