**Example 1: 配置DDoS连接抑制选项**



Input: 

```
tccli antiddos CreateDDoSConnectLimit --cli-unfold-argument  \
    --InstanceId bgpip-00000001 \
    --ConnectLimitConfig.SdNewLimit 0 \
    --ConnectLimitConfig.DstNewLimit 0 \
    --ConnectLimitConfig.SdConnLimit 0 \
    --ConnectLimitConfig.DstConnLimit 0 \
    --ConnectLimitConfig.BadConnThreshold 0 \
    --ConnectLimitConfig.NullConnEnable 0 \
    --ConnectLimitConfig.ConnTimeout 0 \
    --ConnectLimitConfig.SynRate 0 \
    --ConnectLimitConfig.SynLimit 0
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

