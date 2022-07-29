**Example 1: 修改7层监听器转发规则域名**

修改7层监听器转发规则域名

Input: 

```
tccli gaap ModifyDomain --cli-unfold-argument  \
    --OldDomain a.a.com \
    --CertificateId default \
    --ListenerId 0 \
    --NewDomain b.b.com
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

