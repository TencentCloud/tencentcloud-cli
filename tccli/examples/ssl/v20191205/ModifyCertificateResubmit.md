**Example 1: 审核失败证书重新提交申请**

审核失败证书重新提交申请

Input: 

```
tccli ssl ModifyCertificateResubmit --cli-unfold-argument  \
    --CertificateId The**hhs
```

Output: 
```
{
    "Response": {
        "CertificateId": "The**hhs",
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

