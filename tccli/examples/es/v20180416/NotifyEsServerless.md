**Example 1: NotifyEsServerless**



Input: 

```
tccli es NotifyEsServerless --cli-unfold-argument  \
    --ActionTypes abc \
    --SourceInfo.InnerProductType 1 \
    --SourceInfo.InstanceId abc \
    --SourceInfo.LogInfoVersion abc \
    --SourceInfo.ScaleOutCVMInstanceIds abc \
    --SourceInfo.ScaleInCVMInstanceIds abc \
    --SourceInfo.ServiceCvmLogPaths.0.ServiceName abc \
    --SourceInfo.ServiceCvmLogPaths.0.LogPaths abc \
    --SourceInfo.ServiceCvmLogPaths.0.LogIndex abc \
    --SourceInfo.ServiceCvmLogPaths.0.LogFieldRole abc \
    --SourceInfo.ServiceCvmLogPaths.0.LogMultiLinePattern abc
```

Output: 
```
{
    "Response": {
        "DealId": "abc",
        "RequestId": "abc"
    }
}
```

