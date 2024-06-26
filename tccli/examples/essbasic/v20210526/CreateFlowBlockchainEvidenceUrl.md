**Example 1: 生成合同区块链存证证书查看二维码/链接**

拥有访问权限的员工生成合同区块链存证证书查看二维码/链接

Input: 

```
tccli essbasic CreateFlowBlockchainEvidenceUrl --cli-unfold-argument  \
    --Agent.ProxyOperator.OpenId ianc_1111 \
    --Agent.ProxyOrganizationOpenId ABC_organization_open_id \
    --Agent.AppId 16fd2f7d7*****f8d501d57b5ec \
    --FlowId yDCANUUckp******7SI8fHrn0LCd
```

Output: 
```
{
    "Response": {
        "ExpiredOn": 1719463451,
        "QrCode": "https://file.test.ess.tencent.cn/bresource/resource/resource/0/0.JPG?hkey=5d92f0db15e6bbba6aea641f64c5c06d7914ff197f4b2b099ab565a5733**************3a5b2d692827ec738d02a519c7a9f",
        "RequestId": "s17188843684971",
        "Url": "https://test.essurl.cn/SR0****F9B"
    }
}
```

