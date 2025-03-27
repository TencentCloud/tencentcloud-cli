**Example 1: CreateAlarmShield示例1**



Input: 

```
tccli monitor CreateAlarmShield --cli-unfold-argument  \
    --LoopStartDate 1648742400 \
    --StartTime 36000 \
    --NameSpace cvm_device \
    --Module monitor \
    --ShieldMetric CpuUsage \
    --LoopEndDate 1649088000 \
    --ShieldTimeType LOOP_SHIELD \
    --MonitorType MT_QCE \
    --EndTime 72000 \
    --ShieldObject cafka-xxx \
    --Name 1311
```

Output: 
```
{
    "Response": {
        "RequestId": "f4f51ecc-c3fa-4e0a-a9b5-093b1a58013e",
        "ShieldId": "Shield-wixc9u804z"
    }
}
```

**Example 2: 创建告警屏蔽规则**



Input: 

```
tccli monitor CreateAlarmShield --cli-unfold-argument  \
    --Module monitor \
    --Name 测试屏蔽 \
    --MonitorType MT_QCE \
    --NameSpace cvm_device \
    --ShieldObject cafka-xxx cafka-xxx1 \
    --ShieldMetric CpuUsage BaseCpuUsage \
    --ShieldTimeType LOOP_SHIELD \
    --StartTime 36000 \
    --EndTime 72000 \
    --LoopStartDate 1648742400 \
    --LoopEndDate 1649088000
```

Output: 
```
{
    "Response": {
        "RequestId": "29ghj2hh-45-266627r66hheh-23",
        "ShieldId": "shield-xxxx"
    }
}
```

