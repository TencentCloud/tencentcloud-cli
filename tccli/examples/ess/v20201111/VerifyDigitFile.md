**Example 1: 加签文件验证成功示例**

1.填入加签后的文件Id，对文件进行验证

Input: 

```
tccli ess VerifyDigitFile --cli-unfold-argument  \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --FileId yDwFdUUckpsveo27UEQPEVo14KnASuGI
```

Output: 
```
{
    "Response": {
        "PdfResourceMd5": "213CA8C1C84B7BAA73F6FD3959C2F079",
        "RequestId": "s1739352792186436957",
        "VerifyDigitFileResults": [
            {
                "CertNotAfter": 1754852419000,
                "CertNotBefore": 1723316419000,
                "CertSn": "2201c8e9cdd3abb6",
                "SignAlgorithm": "SHA256withRSA",
                "SignTime": 1737103505000,
                "SignType": 1,
                "SignerName": "ESS@XXXXX责任公司测试@662001"
            }
        ],
        "VerifyResult": 1,
        "VerifySerialNo": "17393527923979"
    }
}
```

