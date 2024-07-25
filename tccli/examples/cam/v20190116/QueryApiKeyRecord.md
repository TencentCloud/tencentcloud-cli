**Example 1: 查询密钥访问记录**

查询指定接口访问的服务和接口记录

Input: 

```
tccli cam QueryApiKeyRecord --cli-unfold-argument  \
    --ApiKey AKID****
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Product": "cvm",
                "Action": "GetTestInstance",
                "Cnt": 12,
                "UpdateTime": "2023-05-18 00:18:03"
            }
        ],
        "TotalNum": 1,
        "RequestId": "5205360d-2995-4034-858c-13aee99bef09"
    }
}
```

