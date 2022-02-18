**Example 1: 关闭数据库代理**



Input: 

```
tccli cdb CloseCDBProxy --cli-unfold-argument  \
    --InstanceId cdb-test \
    --ProxyGroupId proxy-test \
    --OnlyCloseRW True
```

Output: 
```
{
    "Response": {
        "RequestId": "3689c0eb-a92d-77ce-0ee2-17d99f604e64"
    }
}
```

