**Example 1: 分页查询产品列表**

查询腾讯云可观测平台产品列表

Input: 

```
tccli monitor DescribeProductList --cli-unfold-argument  \
    --Limit 5 \
    --Module monitor \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ProductList": [
            {
                "ProductName": "私有网络-NAT网关",
                "ProductEnName": "NAT Gateway",
                "Namespace": "qce/nat_qos_stats"
            },
            {
                "ProductName": "CDN-CDN域名国内",
                "ProductEnName": "CDN-China_CDN_Domain",
                "Namespace": "qce/cdn"
            },
            {
                "ProductName": "CDN-CDN项目国内",
                "ProductEnName": "CDN-China_CDN_Project",
                "Namespace": "qce/cdn"
            },
            {
                "ProductName": "云服务器-基础监控",
                "ProductEnName": "Cloud Virtual Machine",
                "Namespace": "qce/cvm"
            },
            {
                "ProductName": "专线接入-物理专线",
                "ProductEnName": "Physical dedicated line",
                "Namespace": "qce/dc"
            }
        ],
        "RequestId": "28b84e33-8865-4cd3-a4ac-bdacccefbb2d",
        "TotalCount": 446
    }
}
```

