**Example 1: Creating flow logs**



Input: 

```
tccli vpc CreateFlowLog --cli-unfold-argument  \
    --CloudLogId xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx\
    --FlowLogDescription test-flowlog\
    --FlowLogName test\
    --ResourceId eni-xxxxxxxx\
    --ResourceType NETWORKINTERFACE\
    --TrafficType ACCEPT\
    --VpcId vpc-xxxxxx
```

Output: 
```
{
    "Response": {
        "FlowLog": [
            {
                "VpcId": "vpc-pq9vxykj",
                "FlowLogId": "fl-f42uhpkj",
                "FlowLogName": "test",
                "ResourceType": "NETWORKINTERFACE",
                "ResourceId": "eni-78ysaex1",
                "TrafficType": "ACCEPT",
                "CloudLogId": "dfb8f1a2-8522-47c1-8571-67905167ab3f",
                "CloudLogState": "",
                "FlowLogDescription": "",
                "TagSet": [
                    {
                        "Key": "city",
                        "Value": "shanghai"
                    }
                ],
                "CreatedTime": "0000-00-00 00:00:00"
            }
        ],
        "RequestId": "404428db-f850-40c2-803"
    }
}
```

