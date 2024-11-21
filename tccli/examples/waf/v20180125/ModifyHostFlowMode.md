**Example 1: 设置负载均衡型WAF防护域名的流量模式**

设置负载均衡型WAF防护域名的流量模式，切换镜像模式和清洗模式

Input: 

```
tccli waf ModifyHostFlowMode --cli-unfold-argument  \
    --Domain "watx.qcloudwaf.com" \
    --DomainId "waf-gi944uHt" \
    --FlowMode 1 \
    --InstanceID "waf_vhhf12q6ntyb"
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

