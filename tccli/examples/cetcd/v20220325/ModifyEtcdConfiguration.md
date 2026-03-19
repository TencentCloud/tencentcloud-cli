**Example 1: 修改etcd实例配置**



Input: 

```
tccli cetcd ModifyEtcdConfiguration --cli-unfold-argument  \
    --InstanceId etcd-abcd1234 \
    --AutoCompactionSettings.AutoCompactionRetention 2h \
    --AutoCompactionSettings.AutoCompactionMode period \
    --MonitorSettings.ExistedPrometheusInstanceId prom-abcd1234
```

Output: 
```
{
    "Response": {
        "RequestId": "abcdefg"
    }
}
```

