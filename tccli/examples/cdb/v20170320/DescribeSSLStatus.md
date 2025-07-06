**Example 1: 获取 SSL 开通情况以及证书下载链接**



Input: 

```
tccli cdb DescribeSSLStatus --cli-unfold-argument  \
    --InstanceId cdb-je5dfmdl
```

Output: 
```
{
    "Response": {
        "Status": "ON",
        "Url": "http://***download.url",
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7"
    }
}
```

