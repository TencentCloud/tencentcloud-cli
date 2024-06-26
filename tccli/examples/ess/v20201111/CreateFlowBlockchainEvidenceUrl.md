**Example 1: 生成合同区块链存证证书查看二维码/链接**

拥有访问权限的员工生成合同区块链存证证书查看二维码/链接

Input: 

```
tccli ess CreateFlowBlockchainEvidenceUrl --cli-unfold-argument  \
    --Operator.UserId yDR0fUUgyg*********jE1RTDui4pB \
    --FlowId yDCANUUc************SI8fHrn0LCd
```

Output: 
```
{
    "Response": {
        "ExpiredOn": 1719463451,
        "QrCode": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.JPG?hkey=5d92f0db15e6bbba6aea641f64c5c06d7914ff197f4b2b0*********27ec738d02a519c7a9f",
        "RequestId": "s1718858684971",
        "Url": "https://test.essurl.cn/SR0*****HF9B"
    }
}
```

