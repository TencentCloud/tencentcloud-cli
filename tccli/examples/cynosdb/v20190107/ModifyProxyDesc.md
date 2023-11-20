**Example 1: 修改数据库代理描述**

修改数据库代理描述

Input: 

```
tccli cynosdb ModifyProxyDesc --cli-unfold-argument  \
    --ClusterId cynosdbmysql-12qwasdf \
    --ProxyGroupId cynosdbmysql-proxy-1qasdfre \
    --Description proxy for test
```

Output: 
```
{
    "Response": {
        "RequestId": "128046"
    }
}
```

