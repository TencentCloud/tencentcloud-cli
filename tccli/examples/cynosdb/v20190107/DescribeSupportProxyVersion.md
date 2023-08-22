**Example 1: 查询支持的数据库代理版本**

查询支持的数据库代理版本

Input: 

```
tccli cynosdb DescribeSupportProxyVersion --cli-unfold-argument  \
    --ClusterId cynosdbmysql-abc \
    --ProxyGroupId cynosdbmysql-proxy-abc
```

Output: 
```
{
    "Response": {
        "SupportProxyVersions": [
            "abc"
        ],
        "CurrentProxyVersion": "abc",
        "RequestId": "abc"
    }
}
```

