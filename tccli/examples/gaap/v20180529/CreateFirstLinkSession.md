**Example 1: 创建接入段加速会话**



Input: 

```
tccli gaap CreateFirstLinkSession --cli-unfold-argument  \
    --TemplateId flt-4av6kul7 \
    --DestAddressInfo.DestIp 143.244.174.31 \
    --SrcAddressInfo.SrcIpv4 10.51.105.127 \
    --SrcAddressInfo.SrcPublicIpv4 211.97.128.200
```

Output: 
```
{
    "Response": {
        "SessionId": "ZWViYzAwNzJmNjRkNGExMDgyMjkzZTY0YzU0ZjZhNDY=-1-0",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Duration": 1790
    }
}
```

