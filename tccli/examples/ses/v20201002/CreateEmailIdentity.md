**Example 1: 创建发信域名**



Input: 

```
tccli ses CreateEmailIdentity --cli-unfold-argument  \
    --EmailIdentity mail.qcloud.com
```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "IdentityType": "DOMAIN",
        "VerifiedForSendingStatus": false,
        "Attributes": [
            {
                "Type": "TXT",
                "SendDomain": "mail.qcloud.com",
                "ExpectedValue": "v=spf1 include:qcloudmail.com ~all",
                "CurrentValue": "",
                "Status": false
            },
            {
                "Type": "TXT",
                "SendDomain": "mail._domainkey.mail.qcloud.com",
                "ExpectedValue": "k=rsa;p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDeMVIzrCa3T14JsNY0IRv5/2V1/v2itlviLQBwXsa7shBD6TrBkswsFUToPyMRWC9tbR/5ey0nRBH0ZVxp+lsmTxid2Y2z+FApQ6ra2VsXfbJP3HE6wAO0YTVEJt1TmeczhEd2Jiz/fcabIISgXEdSpTYJhb0ct0VJRxcg4c8c7wIDAQAB",
                "CurrentValue": "",
                "Status": false
            }
        ]
    }
}
```

