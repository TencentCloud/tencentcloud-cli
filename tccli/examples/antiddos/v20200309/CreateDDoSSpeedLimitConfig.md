**Example 1: 添加DDoS防护的访问限速配置**



Input: 

```
tccli antiddos CreateDDoSSpeedLimitConfig --cli-unfold-argument  \
    --InstanceId bgpip-0000011x \
    --DDoSSpeedLimitConfig.Mode 1 \
    --DDoSSpeedLimitConfig.ProtocolList TCP;UDP \
    --DDoSSpeedLimitConfig.DstPortList 80;443;1000-2000 \
    --DDoSSpeedLimitConfig.SpeedValues.0.Type 1 \
    --DDoSSpeedLimitConfig.SpeedValues.0.Value 1000 \
    --DDoSSpeedLimitConfig.SpeedValues.1.Type 2 \
    --DDoSSpeedLimitConfig.SpeedValues.1.Value 30000000
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

