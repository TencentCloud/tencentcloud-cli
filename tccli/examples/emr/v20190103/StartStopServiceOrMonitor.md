**Example 1: StartStopServiceOrMonitor**

启停服务接口

Input: 

```
tccli emr StartStopServiceOrMonitor --cli-unfold-argument  \
    --InstanceId emr-4zvc5mul \
    --OpType StartService \
    --OpScope.ServiceInfoList.0.ServiceName abc \
    --OpScope.ServiceInfoList.0.ComponentInfoList.0.ComponentName ZKFailoverController \
    --OpScope.ServiceInfoList.0.ComponentInfoList.0.IpList 172.16.114.126 \
    --StrategyConfig.RollingRestartSwitch 0 \
    --StrategyConfig.BatchSize 1 \
    --StrategyConfig.TimeWait 5 \
    --StrategyConfig.DealOnFail 0
```

Output: 
```
{
    "Response": {
        "RequestId": "4c141dbb-b365-4c1b-a209-2c18e47fdb11"
    }
}
```

