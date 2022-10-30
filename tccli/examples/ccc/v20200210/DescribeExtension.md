**Example 1: 获取话机信息**



Input: 

```
tccli ccc DescribeExtension --cli-unfold-argument  \
    --SdkAppId 140000000 \
    --ExtensionId 1001
```

Output: 
```
{
    "Response": {
        "RequestId": "86a17f0e-bcb3-46bf-ac66-8f165fe52127",
        "ExtensionId": "1001",
        "ExtensionDomain": "1400000214.tccc.qcloud.com",
        "Password": "0pMnxfdsdLT6G",
        "OutboundProxy": "sip.tccc.qcloud.com:5061",
        "Transport": "tls"
    }
}
```

