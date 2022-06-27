**Example 1: 创建按量 Prometheus 实例**



Input: 

```
tccli monitor CreatePrometheusMultiTenantInstancePostPayMode --cli-unfold-argument  \
    --SubnetId subnet-hjkasfd \
    --DataRetentionTime 30 \
    --VpcId vpc-thnssd \
    --InstanceName my-prom-gg \
    --Zone ap-chengdu-1 \
    --GrafanaInstanceId grafana-xfa222
```

Output: 
```
{
    "Response": {
        "InstanceId": "prom-xxxxxx",
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

