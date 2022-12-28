**Example 1: 锁定域名**

 

Input: 

```
tccli dnspod ModifyDomainLock --cli-unfold-argument  \
    --Domain dnspod.site \
    --DomainId 62 \
    --LockDays 30
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166",
        "LockInfo": {
            "DomainId": 62,
            "LockCode": "M3xkbnNwb2Quc2l0ZXwxNjE3MzMwODMwfDhlMTkyODZlOGJjMjU4MDBlNjVlZDA1NDFhZjM4NzJm",
            "LockEnd": "2021-05-02"
        }
    }
}
```

