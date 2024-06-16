**Example 1: 获取地域封禁配置**



Input: 

```
tccli waf DescribeAreaBanAreas --cli-unfold-argument  \
    --Domain test.qcloudwaf.com
```

Output: 
```
{
    "Response": {
        "Data": {
            "Areas": [
                "新疆",
                "江西"
            ],
            "Status": "0"
        },
        "RequestId": "5ae9f295-4075-4472-8fd5-da69cc6ffa58"
    }
}
```

**Example 2: 未设置封禁区域的场景**



Input: 

```
tccli waf DescribeAreaBanAreas --cli-unfold-argument  \
    --Domain www.test.com
```

Output: 
```
{
    "Response": {
        "Data": null,
        "RequestId": "7b9c4e2b-8282-4a6a-90cf-f64f2caef67a"
    }
}
```

