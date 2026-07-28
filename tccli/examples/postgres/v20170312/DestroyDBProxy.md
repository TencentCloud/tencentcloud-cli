**Example 1: 销毁数据库代理**

销毁指定数据库代理实例

Input: 

```
tccli postgres DestroyDBProxy --cli-unfold-argument  \
    --DBInstanceId postgres-ll68q8z3 \
    --ProxyGroupId proxygroup-1x2edzxh
```

Output: 
```
{
    "Response": {
        "RequestId": "ba9bf5a6-907a-43de-b81b-41c7430c1f6c"
    }
}
```

