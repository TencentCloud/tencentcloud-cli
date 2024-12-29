**Example 1: 查询服务API列表**

查询微服务API列表

Input: 

```
tccli tsf DescribeMsApiList --cli-unfold-argument  \
    --MicroserviceId ms-y5w8n5e9 \
    --SearchWord echo-feign-url \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "17a35767-819f-4683-bc3f-5430e6d4513f",
        "Result": {
            "Content": [
                {
                    "Description": "",
                    "Method": "GET",
                    "Path": "/echo-feign-url/{str}",
                    "Status": 1
                }
            ],
            "TotalCount": 1
        }
    }
}
```

