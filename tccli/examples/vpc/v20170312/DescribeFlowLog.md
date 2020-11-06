**Example 1: Querying the flow log instance information**



Input: 

```
tccli vpc DescribeFlowLog --cli-unfold-argument  \
    --VpcId vpc-xxxxx \
    --FlowLogId fl-xxxxxx
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
            }
        ],
        "RequestId": "404428db-f850-40c2-803d-0aae49aba43a"
    }
}
```

