**Example 1: 修改 Prometheus 实例相关属性**



Input: 

```
tccli monitor ModifyPrometheusInstanceAttributes --cli-unfold-argument  \
    --InstanceId prom-2rsas2 \
    --InstanceName my-prom-gg
```

Output: 
```
{
    "Response": {
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

**Example 2: 修改 Prometheus 实例存储时长与归档存储时长**



Input: 

```
tccli monitor ModifyPrometheusInstanceAttributes --cli-unfold-argument  \
    --InstanceId prom-2rsas2 \
    --DataRetentionTime 30 \
    --InstanceAttributes.0.Key LongTermStorageRetentionTime \
    --InstanceAttributes.0.Value 90
```

Output: 
```
{
    "Response": {
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

