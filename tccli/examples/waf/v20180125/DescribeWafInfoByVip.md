**Example 1: 通过VIP获取用户信息**

只获取用户信息不获取域名信息

Input: 

```
tccli waf DescribeWafInfoByVip --cli-unfold-argument  \
    --Vip 43.136.161.194
```

Output: 
```
{
    "Response": {
        "Info": {
            "Appid": 251240572,
            "Customer": "cle-dev2",
            "DomainInfo": null,
            "Uin": 700000670233
        },
        "RequestId": "d3552839-6a24-43b2-9f47-4589c7e37532"
    }
}
```

