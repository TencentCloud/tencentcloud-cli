**Example 1: 查询恶意请求白名单列表**

查询恶意请求白名单列表

Input: 

```
tccli cwp DescribeMaliciousRequestWhiteList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "f1dd9f5e-4ac0-48a7-9410-c86d24656d9a",
        "TotalCount": 100,
        "List": [
            {
                "Mark": "备注1",
                "Id": 1,
                "Domain": "dnakdnak",
                "CreateTime": "2021-02-08 14:46:25",
                "ModifyTime": "2021-02-08 14:46:25"
            }
        ]
    }
}
```

