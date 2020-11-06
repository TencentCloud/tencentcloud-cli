**Example 1: 获取流量镜像接收机健康状态**



Input: 

```
tccli bmlb DescribeTrafficMirrorReceiverHealthStatus --cli-unfold-argument  \
    --TrafficMirrorId bmtm-lmep0eit \
    --ReceiverSet.0.InstanceId tcpm-px13l9jh \
    --ReceiverSet.0.Port 113 \
    --ReceiverSet.1.InstanceId tcpm-px13l9jh \
    --ReceiverSet.1.Port 114
```

Output: 
```
{
    "Response": {
        "ReceiversStatusSet": [
            {
                "LanIp": "10.1.100.5",
                "ReceiversPortStatusSet": [
                    {
                        "Port": 113,
                        "Status": "Dead"
                    },
                    {
                        "Port": 114,
                        "Status": "Dead"
                    }
                ]
            }
        ],
        "RequestId": "50bd45da-43ef-4ca2-a396-a37a17978a78"
    }
}
```

