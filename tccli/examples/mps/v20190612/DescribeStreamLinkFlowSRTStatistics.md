**Example 1: 请求示例**



Input: 

```
tccli mps DescribeStreamLinkFlowSRTStatistics --cli-unfold-argument  \
    --FlowId 0175723949ba0956b92d0bf40cfe \
    --StartTime 2020-12-10T11:00:00Z \
    --EndTime 2020-12-10T12:00:00Z \
    --Period 1min \
    --Type input \
    --Pipeline 0 \
    --InputOutputId 0175723949bb0956b92d0bf40cff
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "SendRetransmissionRate": 0,
                "RecvPacketLossRate": 0,
                "Timestamp": 1607606280,
                "SendPacketDropNumber": 0,
                "RecvPacketDropNumber": 0,
                "RTT": 17,
                "SessionId": "xx",
                "SendPacketLossRate": 0,
                "RecvRetransmissionRate": 0
            }
        ],
        "RequestId": "137253816"
    }
}
```

