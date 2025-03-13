**Example 1: 通过部署组ID获取微服务**



Input: 

```
tccli tsf DescribeMicroservicesByGroupIds --cli-unfold-argument  \
    --GroupIds group-6a7eb39y group-nalb5dwv
```

Output: 
```
{
    "Response": {
        "RequestId": "3b3b8c47-e7fa-4938-b9a3-cd2c962de722",
        "Result": {
            "Content": [
                {
                    "CreateTime": null,
                    "CriticalInstanceCount": null,
                    "MicroserviceDesc": null,
                    "MicroserviceId": "ms-yrkd4dla",
                    "MicroserviceName": "consumer-demo",
                    "NamespaceId": "namespace-9yn23x4y",
                    "RunInstanceCount": 1,
                    "UpdateTime": null
                },
                {
                    "CreateTime": null,
                    "CriticalInstanceCount": null,
                    "MicroserviceDesc": null,
                    "MicroserviceId": "ms-ymbjjl3v",
                    "MicroserviceName": "provider-demo",
                    "NamespaceId": "namespace-4y4g8pyk",
                    "RunInstanceCount": 1,
                    "UpdateTime": null
                }
            ],
            "TotalCount": 2
        }
    }
}
```

