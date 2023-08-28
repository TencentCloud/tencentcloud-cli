**Example 1: 查询应用白名单列表**



Input: 

```
tccli bcrpc DescribeSecurityList --cli-unfold-argument  \
    --Name abc
```

Output: 
```
{
    "Response": {
        "AllowedWebsite": [
            "abc"
        ],
        "AllowedIpAddress": [
            "ac"
        ],
        "RequestId": "abc"
    }
}
```

