**Example 1: 获取微服务列表**



Input: 

```
tccli tsf DescribeMicroservices --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1 \
    --NamespaceId namespace-xxxxxxx \
    --SearchWord ms-xxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "3eab4695-2d7e-4f78-a8d2-ea93bab87dfd",
        "Result": {
            "TotalCount": 1,
            "Content": [
                {
                    "MicroserviceId": "ms-xxxxxxx",
                    "NamespaceId": "namespace-xxxxxxx",
                    "MicroserviceName": "consumer-demo",
                    "MicroserviceDesc": null,
                    "CreateTime": 1553673084000,
                    "UpdateTime": 1553673084000,
                    "RunInstanceCount": 1
                }
            ]
        }
    }
}
```

