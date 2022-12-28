**Example 1: 创建域名别名**

 

Input: 

```
tccli dnspod CreateDomainAlias --cli-unfold-argument  \
    --Domain myfm.cc \
    --DomainAlias cc.cc
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "DomainAliasId": 16080
    }
}
```

