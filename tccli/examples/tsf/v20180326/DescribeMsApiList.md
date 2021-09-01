**Example 1: 查询服务API列表**

查询微服务API列表

Input: 

```
tccli tsf DescribeMsApiList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --MicroserviceId ms-opy5kjy4
```

Output: 
```
{
    "Response": {
        "RequestId": "056cc966-4963-4506-ac4c-c4e7209a41e3",
        "Result": {
            "TotalCount": 4,
            "Content": [
                {
                    "Path": "/echo-async-rest/{str}",
                    "Method": "GET",
                    "Description": "(无)"
                },
                {
                    "Path": "/echo-rest/{str}",
                    "Method": "GET",
                    "Description": "(无)"
                },
                {
                    "Path": "/user-feign",
                    "Method": "GET",
                    "Description": "(无)"
                },
                {
                    "Path": "/echo-feign/{str}",
                    "Method": "GET",
                    "Description": "(无)"
                }
            ]
        }
    }
}
```

