**Example 1: 获取微服务列表**



Input: 

```
tccli tsf DescribeMicroservices --cli-unfold-argument  \
    --SearchWord consumer \
    --NamespaceId namespace-v6b2exey \
    --OrderBy create_time \
    --OrderType 1 \
    --Offset 0 \
    --Limit 10 \
    --Status single_online \
    --MicroserviceIdList ms-yqwbbpxl \
    --MicroserviceNameList consumer-demo
```

Output: 
```
{
    "Response": {
        "RequestId": "31c18b1c-4e2e-4cb1-8b82-de820d178f12",
        "Result": {
            "Content": [
                {
                    "CreateTime": null,
                    "CriticalInstanceCount": 0,
                    "MicroserviceDesc": "",
                    "MicroserviceId": "ms-yqwbbpxl",
                    "MicroserviceName": "consumer-demo",
                    "NamespaceId": "namespace-v6b2exey",
                    "RunInstanceCount": 1,
                    "UpdateTime": null
                }
            ],
            "TotalCount": 1
        }
    }
}
```

