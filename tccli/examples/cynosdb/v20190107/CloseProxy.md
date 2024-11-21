**Example 1: 关闭数据库代理**

关闭数据库代理

Input: 

```
tccli cynosdb CloseProxy --cli-unfold-argument  \
    --ClusterId cynosdbmysql-mwg7212w \
    --ProxyGroupId cynosdbmysql-proxy-4378e0ky \
    --OnlyCloseRW True
```

Output: 
```
{
    "Response": {
        "FlowId": 358874,
        "TaskId": 1063084,
        "RequestId": "e4f4f48a-51b1-45be-a9e3-09f0d1412659"
    }
}
```

