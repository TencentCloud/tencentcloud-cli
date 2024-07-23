**Example 1: 获取云架构产品列表**



Input: 

```
tccli advisor DescribeProductList --cli-unfold-argument  \
    --Type  \
    --PluginKey xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "b90a5cc7-1a1e-4fcd-a7ee-46f767be7b38",
        "ProductList": [
            {
                "ProductId": "acl",
                "SigmaId": "ACL",
                "TsaProductId": "acl",
                "ProductName": "网络ACL",
                "IsRegional": true
            },
            {
                "ProductId": "apigw",
                "SigmaId": "API",
                "TsaProductId": "apigw",
                "ProductName": "API 网关",
                "IsRegional": true
            },
            {
                "ProductId": "as",
                "SigmaId": "AS",
                "TsaProductId": "as",
                "ProductName": "弹性伸缩",
                "IsRegional": true
            },
            {
                "ProductId": "bgp",
                "SigmaId": "DDoS",
                "TsaProductId": "bgp",
                "ProductName": "DDos 防护",
                "IsRegional": true
            },
            {
                "ProductId": "bgpip",
                "SigmaId": "DDoS Pro Anti-IP",
                "TsaProductId": "bgpip",
                "ProductName": "DDoS 高防 IP",
                "IsRegional": true
            },
            {
                "ProductId": "bwp",
                "SigmaId": "BWP",
                "TsaProductId": "bwp",
                "ProductName": "共享带宽包 BWP",
                "IsRegional": true
            },
            {
                "ProductId": "cbs",
                "SigmaId": "CBS",
                "TsaProductId": "cbs",
                "ProductName": "云硬盘",
                "IsRegional": true
            },
            {
                "ProductId": "cdb",
                "SigmaId": "CDB",
                "TsaProductId": "mysql",
                "ProductName": "云数据库 MYSQL",
                "IsRegional": true
            },
            {
                "ProductId": "cdn",
                "SigmaId": "CDN",
                "TsaProductId": "cdn",
                "ProductName": "内容分发网络",
                "IsRegional": false
            },
            {
                "ProductId": "cfs",
                "SigmaId": "CFS",
                "TsaProductId": "cfs",
                "ProductName": "文件存储",
                "IsRegional": true
            }
        ]
    }
}
```

