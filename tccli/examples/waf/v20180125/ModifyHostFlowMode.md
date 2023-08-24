**Example 1: 设置防护域名的流量模式**



Input: 

```
tccli waf ModifyHostFlowMode --cli-unfold-argument  \
    --Domain "www.qcloudwaf.com" \
    --DomainId "waf-gi944uHt" \
    --FlowMode 1 \
    --InstanceID "waf_000q6ntyb"
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

