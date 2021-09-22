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
        "RequestId": "req-566234234",
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

