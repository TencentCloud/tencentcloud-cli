**Example 1: 查询所有域名**

查询所有域名的信息。

Input: 

```
tccli vod DescribeVodDomains --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DomainSet": [
            {
                "Domain": "myexample.com",
                "AccelerateAreaInfos": [
                    {
                        "Area": "Internation",
                        "TencentDisableReason": "",
                        "TencentEdgeDomain": "myexmample.com.dnsv1.com"
                    }
                ],
                "RefererAuthPolicy": {
                    "Status": "Disabled",
                    "AuthType": "",
                    "BlankRefererAllowed": "No",
                    "Referers": []
                },
                "DeployStatus": "Deploying",
                "HTTPSConfig": {
                    "CertExpireTime": "2030-01-23T07:25:52Z"
                },
                "UrlSignatureAuthPolicy": {
                    "Status": "Enabled",
                    "EncryptedKey": "acmowmeomeo13432a"
                },
                "CreateTime": "2019-12-23T07:25:52Z",
                "QUICConfig": null
            }
        ],
        "RequestId": "aeomo-133w3-amomow-22"
    }
}
```

