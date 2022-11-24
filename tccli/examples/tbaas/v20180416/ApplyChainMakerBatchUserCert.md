**Example 1: 批量申请长安链用户签名证书**



Input: 

```
tccli tbaas ApplyChainMakerBatchUserCert --cli-unfold-argument  \
    --ClusterId xx \
    --SignUserCsrList.0.CertMark xx \
    --SignUserCsrList.0.SignCsrContent xx
```

Output: 
```
{
    "Response": {
        "SignUserCrtList": [
            "xx"
        ],
        "RequestId": "xx"
    }
}
```

