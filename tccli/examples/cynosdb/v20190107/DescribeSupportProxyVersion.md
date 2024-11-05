**Example 1: 查询支持的数据库代理版本**

查询支持的数据库代理版本

Input: 

```
tccli cynosdb DescribeSupportProxyVersion --cli-unfold-argument  \
    --ClusterId cynosdbmysql-dnofdr2c \
    --ProxyGroupId cynosdbmysql-proxy-4378e0kd
```

Output: 
```
{
    "Response": {
        "SupportProxyVersions": [
            "3.1.4"
        ],
        "CurrentProxyVersion": "3.1.1",
        "SupportProxyVersionDetail": [
            {
                "ProxyVersion": "3.1.5",
                "ProxyVersionType": "BATE"
            }
        ],
        "RequestId": "a5706353-296a-4992-ad07-ac4a48eeba43"
    }
}
```

