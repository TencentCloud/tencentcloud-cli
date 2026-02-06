**Example 1: 创建Splun投递任务**



Input: 

```
tccli cls CreateSplunkDeliver --cli-unfold-argument  \
    --TopicId d1d7d473-827e-4dad-9a42-f0287ad43125 \
    --Name name-test15 \
    --NetInfo.Host 10.0.0.112 \
    --NetInfo.Port 8088 \
    --NetInfo.Token 59f9b80c-ae2f-43c1-8c93-436094343125 \
    --NetInfo.NetType 1 \
    --NetInfo.VpcId vpc-k1bdf0ds \
    --NetInfo.VirtualGatewayType 0 \
    --NetInfo.IsSSL True \
    --MetadataInfo.Format json \
    --IndexAck 1
```

Output: 
```
{
    "Response": {
        "RequestId": "7006acf0-0b04-442d-a09e-1d2925cac79a",
        "TaskId": "65a07eec-96ee-458d-850b-53dfe9b43125"
    }
}
```

