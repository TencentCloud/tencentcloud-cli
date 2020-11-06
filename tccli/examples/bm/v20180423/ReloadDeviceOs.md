**Example 1: 重装操作系统**



Input: 

```
tccli bm ReloadDeviceOs --cli-unfold-argument  \
    --InstanceId cpm-xxx \
    --Password 123456Test \
    --OsTypeId 1 \
    --VpcId vpc-xxxxx \
    --SubnetId subnet-xxxxx \
    --RaidId 2 \
    --IsZoning 1 \
    --SysRootSpace 20 \
    --SysSwaporuefiSpace 10 \
    --SysUsrlocalSpace 10 \
    --LanIp 10.88.255.6 \
    --HyperThreading 1 \
    --NeedSecurityAgent 1 \
    --NeedMonitorAgent 1
```

Output: 
```
{
    "Response": {
        "TaskId": 123,
        "RequestId": "e9825743-cfaf-43a1-85be-9c99966430dd"
    }
}
```

