**Example 1: 创建扩展证书**



Input: 

```
tccli ga2 CreateListenerAdditionalCert --cli-unfold-argument  \
    --GlobalAcceleratorId ga-dpduwq04 \
    --ListenerId lsr-fa2pnafr \
    --AdditionalCertificates N8WDVXxW
```

Output: 
```
{
    "Response": {
        "RequestId": "3e9b45d1-c091-4ebe-aa7f-638b644b1549",
        "TaskId": "ba7175c1-ba55-403f-86c3-717138777a44"
    }
}
```

