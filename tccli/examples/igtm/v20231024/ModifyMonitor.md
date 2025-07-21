**Example 1: 修改监控器**

修改监控器

Input: 

```
tccli igtm ModifyMonitor --cli-unfold-argument  \
    --MonitorId 1 \
    --MonitorName 测试监控器 \
    --CheckProtocol PING \
    --CheckInterval 1 \
    --Timeout 1 \
    --FailTimes 1 \
    --FailRate 1 \
    --DetectorStyle AUTO \
    --DetectorGroupIds 1 \
    --PingNum 1 \
    --TcpPort 1 \
    --Host url \
    --Path /path \
    --ReturnCodeThreshold 1 \
    --EnableRedirect DISABLED \
    --EnableSni DISABLED \
    --PacketLossRate 1
```

Output: 
```
{
    "Response": {
        "Msg": "success",
        "RequestId": "8f0325a8-4dd6-4fcb-8f6b-c45e587e51b0"
    }
}
```

