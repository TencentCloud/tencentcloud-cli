**Example 1: 查询扫码登录配置**

查询扫码登录配置

Input: 

```
tccli cwp DescribeLoginTypeGlobalConf --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Enable": 1,
        "ExcludeHostCount": 152,
        "ExcludeQuuid": [],
        "IncludeHostCount": 4,
        "IncludeQuuid": [
            "3210d9d5-13ce-4f21-a333-03a2c6e2b010",
            "f4a8f409-0048-4c91-a58f-165750b2dc00",
            "01fa34d3-db26-48ab-9f14-e8d3a48be95e",
            "480419ed-5477-4666-ac09-97bd49be4f7a"
        ],
        "EnableCount": 10,
        "DisableCount": 0,
        "RequestId": "cbbdcf2e-2d9f-424f-ad6c-e5ba1c33a88b",
        "Scope": 0
    }
}
```

