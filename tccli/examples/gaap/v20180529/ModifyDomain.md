**Example 1: 修改7层监听器转发规则域名**

修改7层监听器转发规则域名

Input: 

```
tccli gaap ModifyDomain --cli-unfold-argument  \
    --ListenerId 0\
    --OldDomain a.a.com\
    --NewDomain b.b.com\
    --CertificateId default
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

