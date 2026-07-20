**Example 1: 替换扩展证书**



Input: 

```
tccli ga2 ReplaceListenerAdditionalCert --cli-unfold-argument  \
    --GlobalAcceleratorId ga-dpduwq04 \
    --ListenerId lsr-fa2pnafr \
    --AdditionalCertificate NMGyDIvx \
    --OldCertificate N8WDVXxW
```

Output: 
```
{
    "Response": {
        "RequestId": "3900382b-9793-466d-9573-cd5116910a31",
        "TaskId": "cb4bad0f-f1de-4a57-8af5-f35927abff3e"
    }
}
```

