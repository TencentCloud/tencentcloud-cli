**Example 1: 创建数据库代理**

为指定 PG 实例创建数据库代理

Input: 

```
tccli postgres CreateDBProxy --cli-unfold-argument  \
    --DBInstanceId postgres-ll68q8z3 \
    --VpcId vpc-evvog2gd \
    --SubnetId subnet-clk8il4i \
    --ProxyNodeCustom.0.NodeCount 2 \
    --ProxyNodeCustom.0.Zone ap-guangzhou-3 \
    --ProxyNodeCustom.0.Cpu 2 \
    --ProxyNodeCustom.0.Mem 4 \
    --SecurityGroup sg-xxxxxxxx \
    --Description test proxy \
    --ConnectionPoolLimit 200
```

Output: 
```
{
    "Response": {
        "DealName": "20260523594022883452641",
        "ProxyGroupId": "proxygroup-1x2edzxh",
        "RequestId": "ba9bf5a6-907a-43de-b81b-41c7430c1f6c"
    }
}
```

