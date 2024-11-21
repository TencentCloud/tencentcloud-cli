**Example 1: StartStopServiceOrMonitor**

启停服务接口

Input: 

```
tccli emr StartStopServiceOrMonitor --cli-unfold-argument  \
    --InstanceId emr-mfk \
    --OpScope.ServiceInfoList.0.ComponentInfoList.0.ComponentName NameNode \
    --OpScope.ServiceInfoList.0.ComponentInfoList.0.IpList 0.0.0.0 \
    --OpScope.ServiceInfoList.0.ComponentInfoList.1.ComponentName ZKFailoverController \
    --OpScope.ServiceInfoList.0.ComponentInfoList.1.IpList 0.0.0.0 \
    --OpScope.ServiceInfoList.0.ServiceName HDFS \
    --OpType StartService
```

Output: 
```
{
    "Response": {
        "RequestId": "017c3a6d-382a-4cb2-bd7d-67072b86f027"
    }
}
```

