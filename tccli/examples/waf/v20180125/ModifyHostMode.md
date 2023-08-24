**Example 1: 设置防护域名防护状态**



Input: 

```
tccli waf ModifyHostMode --cli-unfold-argument  \
    --Domain xx \
    --DomainId xxxx \
    --Mode 21 \
    --Type 1 \
    --InstanceID waf_0e2v15x
```

Output: 
```
{
    "Response": {
        "Success": {
            "Code": "Success",
            "Message": "Success"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

