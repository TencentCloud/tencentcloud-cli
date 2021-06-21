**Example 1: 设置单IP告警阈值配置**



Input: 

```
tccli antiddos CreateIPAlarmThresholdConfig --cli-unfold-argument  \
    --IpAlarmThresholdConfigList.0.AlarmType 1 \
    --IpAlarmThresholdConfigList.0.AlarmThreshold 1000 \
    --IpAlarmThresholdConfigList.0.InstanceDetailList.0.EipList 1.1.1.1 \
    --IpAlarmThresholdConfigList.0.InstanceDetailList.0.InstanceId bgpip-0000011x
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

