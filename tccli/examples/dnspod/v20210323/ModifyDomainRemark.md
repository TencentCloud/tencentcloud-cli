**Example 1: 设置域名备注**

 

Input: 

```
tccli dnspod ModifyDomainRemark --cli-unfold-argument  \
    --Domain dnspod.site \
    --DomainId 62 \
    --Remark 这是XXX专用域名
```

Output: 
```
{
    "Response": {
        "RequestId": "ab4f1426-ea15-42ea-8183-dc1b44151166"
    }
}
```

