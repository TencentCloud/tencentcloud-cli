**Example 1: 查询云监控产品列表**



Input: 

```
tccli monitor DescribeProductList --cli-unfold-argument  \
    --Module monitor \
    --Order DESC \
    --Offset 0 \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "ProductList": [
            {
                "ProductName": "shan_17_01_policy01",
                "ProductEnName": "shan_17_01_policy01",
                "Namespace": "test/17_01"
            },
            {
                "ProductName": "redis测试",
                "ProductEnName": "redis_test",
                "Namespace": "test/redistest"
            },
            {
                "ProductName": "负载均衡-七层集群",
                "ProductEnName": "Cloud Load Banlancer-Layer-7 Cluster",
                "Namespace": "qce/loadbalance"
            },
            {
                "ProductName": "aaaa",
                "ProductEnName": "dddd",
                "Namespace": "min/test23"
            },
            {
                "ProductName": "测试的策略类型",
                "ProductEnName": "testpolicytype",
                "Namespace": "qce/rabbit"
            }
        ],
        "RequestId": "addfaffqqn",
        "TotalCount": 294
    }
}
```

