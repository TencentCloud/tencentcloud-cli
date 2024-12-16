**Example 1: test**

获取单条命名空间记录

Input: 

```
tccli tdmq DescribeRocketMQNamespacesOpt --cli-unfold-argument  \
    --ClusterName tdmq_txy_gz_01 \
    --NamespaceId pulsar-pbkdk57xz9wv/ns_1
```

Output: 
```
{
    "Response": {
        "RequestId": "8754897d-441a-4912-99ea-3894be9f6b88",
        "TotalCount": 1,
        "NamespaceSet": [
            {
                "NamespaceId": "pulsar-pbkdk57xz9wv/ns_1",
                "NamespaceName": "ns_1",
                "CustomerUin": null,
                "CustomerAppId": null,
                "TenantId": "pulsar-pbkdk57xz9wv",
                "TenantName": null,
                "BundleCount": 30,
                "RateInLimit": 12288,
                "RateOutLimit": 50000,
                "ThroughputInLimit": 62914560,
                "ThroughputOutLimit": 51200000,
                "MessageTtl": 1296000,
                "RetentionTime": 0,
                "Metrics": {
                    "RateIn": 0,
                    "RateOut": 0,
                    "ThroughputIn": 0,
                    "ThroughputOut": 0,
                    "StorageSize": 0
                },
                "CreateTime": null,
                "UpdateTime": null,
                "Remark": null
            }
        ]
    }
}
```

