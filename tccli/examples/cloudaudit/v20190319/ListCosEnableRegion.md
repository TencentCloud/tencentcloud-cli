**Example 1: 查询云审计支持的cos可用区**

查询云审计支持的cos可用区

Input: 

```
tccli cloudaudit ListCosEnableRegion --cli-unfold-argument  \
    --WebsiteType zh
```

Output: 
```
{
    "Response": {
        "RequestId": "2e81bc9d-5463-498f-9336-32f814940018",
        "EnableRegions": [
            {
                "CosRegion": "ap-shanghai",
                "CosRegionName": "上海(华东)"
            },
            {
                "CosRegion": "ap-hongkong",
                "CosRegionName": "香港"
            }
        ]
    }
}
```

