**Example 1: 修改tdsql3-6d3cbb0f的SSL状态**



Input: 

```
tccli tdmysql ModifyInstanceSSLStatus --cli-unfold-argument  \
    --InstanceId tdsql3-fx3xmcfghh  \
    --Enabled True \
    --CertificateType Custom \
    --CertificateId ategdHIO
```

Output: 
```
{
    "Response": {
        "FlowId": 4295087399,
        "RequestId": "fcdc3907-6254-4c78-8b2e-77f2310d9e0c"
    }
}
```

