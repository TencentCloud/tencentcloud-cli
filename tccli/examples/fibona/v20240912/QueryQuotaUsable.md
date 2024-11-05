**Example 1: 查询配额示例**

成功请求

Input: 

```
tccli fibona QueryQuotaUsable --cli-unfold-argument  \
    --UserGroupUniqueID 
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": {
            "Usables": [
                {
                    "AmountAvailable": 0,
                    "TypeName": "openai_normal"
                },
                {
                    "AmountAvailable": 0,
                    "TypeName": "openai_pro"
                },
                {
                    "AmountAvailable": 0,
                    "TypeName": "hunyuan"
                },
                {
                    "AmountAvailable": 0,
                    "TypeName": "private"
                }
            ]
        },
        "JSONStrPaths": [],
        "Msg": "success",
        "RequestId": "fdb67864-fcef-492b-9e70-f6bd9461ab56"
    }
}
```

