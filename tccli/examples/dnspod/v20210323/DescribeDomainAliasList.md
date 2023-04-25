**Example 1: 获取域名别名列表**

 

Input: 

```
tccli dnspod DescribeDomainAliasList --cli-unfold-argument  \
    --Domain myfm.cc
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "DomainAliasList": [
            {
                "DomainAlias": "cc.cc",
                "Id": 16063,
                "Status": 2
            }
        ]
    }
}
```

