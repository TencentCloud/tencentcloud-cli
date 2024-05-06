**Example 1: 获取SSL开通情况以及证书下载链接**



Input: 

```
tccli cdb DescribeSSLStatus --cli-unfold-argument  \
    --InstanceId cdb-test
```

Output: 
```
{
    "Response": {
        "Status": "ON",
        "Url": "http://test",
        "RequestId": "xxxx-xxxx-xxxxxx"
    }
}
```

