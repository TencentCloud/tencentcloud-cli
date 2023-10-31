**Example 1: es回调emr日志接入的接口**



Input: 

```
tccli emr NotifyEmr --cli-unfold-argument  \
    --InstanceId emr-effjsx \
    --ActionMethod register \
    --ActionCode 1 \
    --ActionMsg 
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx"
    }
}
```

