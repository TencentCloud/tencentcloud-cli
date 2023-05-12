**Example 1: 吊销证书**

吊销证书

Input: 

```
tccli ssl RevokeCertificate --cli-unfold-argument  \
    --CertificateId a91hoLqi \
    --Reason revoke
```

Output: 
```
{
    "Response": {
        "RevokeDomainValidateAuths": [
            {
                "DomainValidateAuthPath": "/.well-known/pki-validation/",
                "DomainValidateAuthKey": "fileauth.txt",
                "DomainValidateAuthValue": "2020091410184....fvkw2nv1z283lzfi66n",
                "DomainValidateAuthDomain": "abc.com"
            }
        ],
        "RequestId": "91afa3b6-5b67-43e1-b312-9d3b9bf0f410"
    }
}
```

