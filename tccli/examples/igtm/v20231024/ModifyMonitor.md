**Example 1: 修改监控器**

修改监控器

Input: 

```
tccli igtm ModifyMonitor --cli-unfold-argument  \
    --MonitorId 1 \
    --MonitorName test \
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
        "RequestId": "100-222"
    }
}
```

