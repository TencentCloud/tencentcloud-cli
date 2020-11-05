**Example 1: Querying the flow log set**



Input: 

```
tccli vpc DescribeFlowLogs --cli-unfold-argument  \
    --Offset 0\
    --Limit 10
```

Output: 
```
{
    "Response": {
        "FlowLog": [
            {
                "CloudLogId": "219d5186-eab0-4510-905b-84925d8ec35e",
                "CloudLogState": "SUCCESS",
                "CreatedTime": "2019-05-07 18:00:26",
                "FlowLogDescription": "",
                "FlowLogId": "fl-2edhcclz",
                "FlowLogName": "yuemingtest",
                "ResourceId": "eni-78ysaex1",
                "ResourceType": "NETWORKINTERFACE",
                "TrafficType": "ACCEPT",
                "VpcId": "vpc-pq9vxykj"
            },
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
                "VpcId": "vpc-pq9vxykj"
            }
        ],
        "TotalNum": 2,
        "RequestId": "404428db-f850-40c2-803d-0aae49aba43a"
    }
}
```

