**Example 1: 审核失败证书重新提交申请**



Input: 

```
tccli ssl ModifyCertificateResubmit --cli-unfold-argument  \
    --CertificateId xxx
```

Output: 
```
{
    "Response": {
        "CertificateId": "xx",
        "RequestId": "xx"
    }
}
```

