**Example 1: 查询支持的数据库代理版本**



Input: 

```
tccli cynosdb DescribeSupportProxyVersion --cli-unfold-argument  \
    --ClusterId xx
```

Output: 
```
{
    "Response": {
        "SupportProxyVersions": [
            "xx"
        ],
        "CurrentProxyVersion": "0.0",
        "RequestId": "xx"
    }
}
```

