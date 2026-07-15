**Example 1: 删除扩展证书**



Input: 

```
tccli ga2 DeleteListenerAdditionalCert --cli-unfold-argument  \
    --GlobalAcceleratorId ga-dpduwq04 \
    --ListenerId lsr-fa2pnafr \
    --AdditionalCertificates N8WDVXxW
```

Output: 
```
{
    "Response": {
        "RequestId": "88903dc9-c812-44d0-a1cb-5774b6d8859c",
        "TaskId": "833237cf-4a92-42ab-9578-f87ca36034f8"
    }
}
```

