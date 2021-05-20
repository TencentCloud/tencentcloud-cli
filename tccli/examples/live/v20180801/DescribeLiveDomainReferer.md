**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveDomainReferer --cli-unfold-argument  \
    --DomainName 5000.liveplay.myqcloud.com
```

Output: 
```
{
    "Response": {
        "RefererAuthConfig": {
            "DomainName": "5000.liveplay.myqcloud.com",
            "Enable": 1,
            "Type": 0,
            "AllowEmpty": 1,
            "Rules": "xxx.com;yyy.com"
        },
        "RequestId": "8e50cdb5-56dc-408b-89b0-31818958d424"
    }
}
```

