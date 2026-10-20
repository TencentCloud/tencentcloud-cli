**Example 1: 查询数据库代理地域库存**

查询数据库代理地域库存

Input: 

```
tccli cynosdb DescribeProxyZoneStocks --cli-unfold-argument  \
    --Zone ap-guangzhou-3
```

Output: 
```
{
    "Response": {
        "ProxyZoneStockInfos": [
            {
                "Region": "ap-guangzhou",
                "Zone": "ap-guangzhou-3",
                "CpuStock": 124,
                "MemStock": 3192000
            }
        ],
        "RequestId": "bef4efb8-8208-42a7-a007-dc0eda930f68"
    }
}
```

