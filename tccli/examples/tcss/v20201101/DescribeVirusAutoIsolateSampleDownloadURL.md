**Example 1: 查询木马自动隔离样本下载链接**



Input: 

```
tccli tcss DescribeVirusAutoIsolateSampleDownloadURL --cli-unfold-argument  \
    --MD5 dskaldjskld
```

Output: 
```
{
    "Response": {
        "FileUrl": "https://malware-1258344699.cos.ap-guangzhou.myqcloud.com/samples%2F5b98800688cae1533ff965ab31baeab1?q-sign-algorithm=sha1&q-ak=AKID******&q-sign-time=1730427587%3B1730431187&q-key-time=1730427587%3B1730431187&q-header-list=host&q-url-param-list=&q-signature=2aed00b5e98f66d0aeb833036362f98c17c51bd0",
        "RequestId": "56726fc5-1a50-46ba-ba2a-eb5f7aff4cd3"
    }
}
```

