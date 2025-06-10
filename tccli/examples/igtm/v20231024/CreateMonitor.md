**Example 1: tcp监控**

tcp监控

Input: 

```
tccli igtm CreateMonitor --cli-unfold-argument  \
    --MonitorName 监控tcp \
    --CheckProtocol TCP \
    --CheckInterval 60 \
    --Timeout 2 \
    --FailTimes 0 \
    --FailRate 50 \
    --DetectorStyle AUTO \
    --DetectorGroupIds 1 \
    --TcpPort 80
```

Output: 
```
{
    "Response": {
        "MonitorId": 92,
        "RequestId": "ea6eaf52-428b-4d1d-b7d7-1712cf508124"
    }
}
```

**Example 2: http监控**

http监控

Input: 

```
tccli igtm CreateMonitor --cli-unfold-argument  \
    --MonitorName 监控http \
    --CheckProtocol HTTP \
    --CheckInterval 60 \
    --Timeout 2 \
    --FailTimes 0 \
    --FailRate 50 \
    --DetectorStyle AUTO \
    --DetectorGroupIds 1 \
    --TcpPort 80 \
    --ReturnCodeThreshold 400 \
    --EnableRedirect DISABLED \
    --EnableSni DISABLED
```

Output: 
```
{
    "Response": {
        "MonitorId": 93,
        "RequestId": "506ffb0f-a5d4-4b8e-8ce8-14e512ec731e"
    }
}
```

**Example 3: 新增监控器**

新增监控器

Input: 

```
tccli igtm CreateMonitor --cli-unfold-argument  \
    --MonitorName 监控器1 \
    --DetectorGroupIds 5 6 7 \
    --CheckInterval 60 \
    --PacketLossRate 20 \
    --CheckProtocol HTTP \
    --FailRate 20 \
    --TcpPort 80 \
    --EnableSni DISABLED \
    --PingNum 10 \
    --ReturnCodeThreshold 500 \
    --Host test.com \
    --Timeout 50 \
    --Path /index.html \
    --FailTimes 2 \
    --DetectorStyle AUTO
```

Output: 
```
{
    "Response": {
        "MonitorId": 1,
        "RequestId": "ea6eaf52-428b-4d1d-b7d7-1712cf508124"
    }
}
```

**Example 4: 监控器ping协议**

监控器ping协议

Input: 

```
tccli igtm CreateMonitor --cli-unfold-argument  \
    --MonitorName 监控ping \
    --CheckProtocol PING \
    --CheckInterval 60 \
    --Timeout 2 \
    --FailTimes 0 \
    --FailRate 50 \
    --DetectorStyle AUTO \
    --DetectorGroupIds 1 \
    --PingNum 20 \
    --PacketLossRate 10
```

Output: 
```
{
    "Response": {
        "MonitorId": 91,
        "RequestId": "93ba54c1-a533-42bb-aab5-458aef4b1666"
    }
}
```

