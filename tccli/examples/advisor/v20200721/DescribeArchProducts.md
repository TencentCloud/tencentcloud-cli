**Example 1: 获取架构图关联的产品列表**



Input: 

```
tccli advisor DescribeArchProducts --cli-unfold-argument  \
    --ArchId arch-s0di7f4y
```

Output: 
```
{
    "Response": {
        "RequestId": "3d803975-476b-4975-b1a4-38fe2f3b048b",
        "ProductList": [
            "ccn",
            "cdb",
            "cdn",
            "ckafka",
            "clb",
            "cos",
            "css",
            "cvm",
            "dcdb",
            "dnspod",
            "domain",
            "emr",
            "es",
            "mongodb",
            "nat",
            "redis",
            "sms",
            "ssl",
            "tke",
            "trtc",
            "vod",
            "vpnx",
            "waf"
        ]
    }
}
```

