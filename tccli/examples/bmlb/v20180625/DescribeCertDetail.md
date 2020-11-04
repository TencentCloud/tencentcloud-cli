**Example 1: 获取黑石负载均衡证书详情**

获取黑石负载均衡证书详情

Input: 

```
tccli bmlb DescribeCertDetail --cli-unfold-argument  \
    --CertId LnSy875f
```

Output: 
```
{
    "Response": {
        "CertId": "LnSy875f",
        "CertName": "qcloud.com",
        "CertType": "SVR",
        "CertContent": "-----BEGIN CERTIFICATE-----\nMIII6DCCB9CgAwIBAgIMZHBKoJEPtanQGg7tMA0GCSqGSIb3DQEBCwUAMGYxCzAJ\nBgNVBAYTAkJFMRkwFwYDVQQKExBHbG9iYWxTaWduIG52LXNhMTwwOgYDVQQDEzNH\nbG9iYWxTaWduIE9yZ2FuaXphdGlvbiBWYWxpZGF0aW9uIENBIC0gU0hBMjU2IC0g\nRzIwHhcNMTgwMzA4MDMyMTI3WhcNMTkwMzA5MDMyMTI3WjCBhjELMAkGA1UEBhMC\nQ04xEjAQBgNVBAgTCWd1YW5nZG9uZzERMA8GA1UEBxMIc2hlbnpoZW4xNjA0BgNV\nBAoTLVRlbmNlbnQgVGVjaG5vbG9neSAoU2hlbnpoZW4pIENvbXBhbnkgTGltaXRl\nZDEYMBYGA1UEAwwPKi53ZWl4aW4ucXEuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEAv3oip/g2xsRk8mLDbpRV9gsnhpsWjN+ND9akufbBdfjUcEdQ\nU+G7/H7v8udW91nQiosCVXjT4+Hk7n7DykAPCvxlLMyqyPGw/Cjdv7pRMD6iAJkA\nAcnxc9q3PdY9qTvh9NuZd5pbpscWc8owsr/o834cTKdJ43yND/9JoCvavt55/02D\n17jOx8GvRJ/+/X82Cw/qGLkoRWijB+754qnjU/Kv83Xot6Tg1NAMmF0hhAVP3OMi\nZDWsBYHBESoAmNvdmfjD6pFB3xPbVgVaXXbiZDI3eTlZDN63+W9Shh78ShHSC/Nq\noUO0TLOEdI2wVj0Vh3aGflLbXV8s3kjd/foSoQIDAQABo4IFczCCBW8wDgYDVR0P\nAQH/BAQDAgWgMIGgBggrBgEFBQcBAQSBkzCBkDBNBggrBgEFBQcwAoZBaHR0cDov\nL3NlY3VyZS5nbG9iYWxzaWduLmNvbS9jYWNlcnQvZ3Nvcmdhbml6YXRpb252YWxz\naGEyZzJyMS5jcnQwPwYIKwYBBQUHMAGGM2h0dHA6Ly9vY3NwMi5nbG9iYWxzaWdu\nLmNvbS9nc29yZ2FuaXphdGlvbnZhbHNoYTJnMjBWBgNVHSAETzBNMEEGCSsGAQQB\noDIBFDA0MDIGCCsGAQUFBwIBFiZodHRwczovL3d3dy5nbG9iYWxzaWduLmNvbS9y\nZXBvc2l0b3J5LzAIBgZngQwBAgIwCQYDVR0TBAIwADBJBgNVHR8EQjBAMD6gPKA6\nhjhodHRwOi8vY3JsLmdsb2JhbHNpZ24uY29tL2dzL2dzb3JnYW5pemF0aW9udmFs\nc2hhMmcyLmNybDCCAbIGA1UdEQSCAakwggGlgg8qLndlaXhpbi5xcS5jb22CEiou\nY2RuLm15cWNsb3VkLmNvbYIMKi5pLmd0aW1nLmNughMqLmltZ2NhY2hlLmd0aW1n\nLmNughEqLmltZ2NhY2hlLnFxLmNvbYINKi5tYWlsLnFxLmNvbYILKi5tcC5xcS5j\nb22CCyoubXlhcHAuY29tggwqLnFjbG91ZC5jb22CCSoucXBpYy5jboIVKi5xem9u\nZXN0eWxlLmd0aW1nLmNuggwqLnF6cy5xcS5jb22CDCoudGVucGF5LmNvbYIIKi51\ncmwuY26CDCoud2VpeXVuLmNvbYILKi53eC5xcS5jb22CDGFnYW1lLnFxLmNvbYIM\nY2RuLmIucXEuY29tgg5jb21iby5iLnFxLmNvbYIKZDNnLnFxLmNvbYIPaW1nY2Fj\naGUucXEuY29tggxtdXNpYy5xcS5jb22CDXBpbmdqcy5xcS5jb22CDHF6YXBwLnFx\nLmNvbYIRcmVzY2RuLnFxbWFpbC5jb22CCndlaXl1bi5jb22CDHd4aW1nLnFxLmNv\nbYINd2VpeGluLnFxLmNvbTAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIw\nHQYDVR0OBBYEFJ7PcRlhw9bopia4iK4Faet2MjbFMB8GA1UdIwQYMBaAFJbeYfG9\nHBYpUxzAzH07gwBA5hp8MIIB9QYKKwYBBAHWeQIEAgSCAeUEggHhAd8AdaDd6x0r\neg1PpiCLga2BaHB+Lo6dAdVciI09EcTNtuy+zAAAAWIDoLy5AAAEAwBHMEUCIQD3\n+2fVXVpklZQSphL/tVv12ECfTVMCdjAgzHpR9eQBXgIgRRauiZzcQY/ylCS+nfKa\nx3MwuclIvqCjxNXoC/RNKgEAdgBWFAaaL9fC7NP14b1Esj7HRna5vJkRXMDvlJhV\n1onQ3QAAAWIDoLzWAAAEAwBHMEUCIQC2tRT/IPM8otPLbxeps+hk/oJp0zex+1EM\n9R982viawgIgA28CQF5PSbLbbj85oAqVmD9ZG9Vs51s4n3MywgZrEloAdgCkuQmQ\ntBhYFIe7E6LMZ3AKPDWYBPkb37jjd80OyA3cEAAAAWIDoMFhAAAEAwBHMEUCIQDM\nB+BfsROBEUR5NUcb/YxdMXyaKA2xPVvM8x0lTR/qqAIgRDE+vg8dy6SsN7mbwD1C\nmOAZS+jgebgTOKBA8M0PJtEAdQDuS723dc5guuFCaR+r4Z5mow9+X7By2IMAxHuJ\neqj9ywAAAWIDoMJ4AAAEAwBGMEQCIB+KaEpmnB4GMhf4BC15l6HAcs7xnEe/kUtm\nOSES4aF4AiBN2z5qX3u1eifM/iTk3qhVGWYAeJe0d52Btx+MDcR69jANBgkqhkiG\n9w0BAQsFAAOCAQEAq6FnsfFmGX8lYBjuOZK0ugOI027FCwS89ICkBZJWF3pvfv9t\nWSOW7euHza5oCQ36YXfsnLIC9GLr/hlhBYUzyezmx/kv3vstnJoETcAbqY1waFdV\nI1Xss7d4sqp7t1hwNqf9bZkC4E8mgEiuVxatqtLGCmm92kv5Dgs7s2j0+mZg4Wx9\nqQ9TboLzxY5jwD1eqp009ZUqJWQ82dEfbz6GEMo40PbJ3aUWT6Qw2ggUqbPyUlIr\nUJcj34KHKl+n1gqVJ7dA7iTkpSKtVeMig3eRsrWw9D7oeqfXaJ5jjDdxhL2CEx8H\nWRKyOmSpWc2fG/b9MxuXpztJTzYTs+DpTjdysg==\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIEaTCCA1GgAwIBAgILBAAAAAABRE7wQkcwDQYJKoZIhvcNAQELBQAwVzELMAkG\nA1UEBhMCQkUxGTAXBgNVBAoTEEdsb2JhbFNpZ24gbnYtc2ExEDAOBgNVBAsTB1Jv\nb3QgQ0ExGzAZBgNVBAMTEkdsb2JhbFNpZ24gUm9vdCBDQTAeFw0xNDAyMjAxMDAw\nMDBaFw0yNDAyMjAxMDAwMDBaMGYxCzAJBgNVBAYTAkJFMRkwFwYDVQQKExBHbG9i\nYWxTaeduIG52LXNhMTwwOgYDVQQDEzNHbG9iYWxTaWduIE9yZ2FuaXphdGlvbiBW\nYWxpZGF0aW9uIENBIC0gU0hBMjU2IC0gRzIwggEiMA0GCSqGSIb3DQEBAQUAA4IB\nDwAwggEKAoIBAQDHDmw/I5N/zHClnSDDDlM/fsBOwphJykfVI+8DNIV0yKMCLkZc\nC33JiJ1Pi/D4nGyMVTXbv/Kz6vvjVudKRtkTIso21ZvBqOOWQ5PyDLzm+ebomchj\nSHh/VzZpGhkdWtHUfcKc1H/hgBKueuqI6lfYygoKOhJJomIZeg0k9zfrtHOSewUj\nmxK1zusp36QUArkBpdSmnENkiN74fv7j9R7l/tyjqORmMdlMJekYuYlZCa7pnRxt\nNw9KHjUgKOKv1CGLAcRFrW4rY6uSa2EKTSDtc7p8zv4WtdufgPDWi2zZCHlKT3hl\n2pK8vjX5s8T5J4BO/5ZS5gIg4Qdz6V0rvbLxAgMBAAGjggElMIIBITAOBgNVHQ8B\nAf8EBAMCAQYwEgYDVR0TAQH/BAgwBgEB/wIBADAdBgNVHQ4EFgQUlt5h8b0cFilT\nHMDMfTuDAEDmGnwwRwYDVR0gBEAwPjA8BgRVHSAAMDQwMgYIKwYBBQUHAgEWJmh0\ndHBzOi8vd3d3Lmdsb2JhbHNpZ24uY29tL3JlcG9zaXRvcnkvMDMGA1UdHwQsMCow\nKKAmoCSGImh0dHA6Ly9jcmwuZ2xvYmFsc2lnbi5uZXQvcm9vdC5jcmwwPQYIKwYB\nBQUHAQEEMTAvMC0GCCsGAQUFBzABhiFodHRwOi8vb2NzcC5nbG9iYWxzaWduLmNv\nbS9yb290cjEwHwYDVR0jBBgwFoAUYHtmGkUNl8qJUC99BM00qP/8/UswDQYJKoZI\nhvcNAQELBQADggEBAEYq7l69rgFgNzERhnF0tkZJyBAW/i9iIxerH4f4gu3K3w4s\n32R1juUYcqeMOovJrKV3UPfvnqTgoI8UV6MqX+x+bRDmuo2wCId2Dkyy2VG7EQLy\nXN0cvfNVlg/UBsD84iOKJHDTu/B5GqdhcIOKrwbFINihY9Bsrk8y1658GEV1BSl3\n30JAZGSGvip2CTFvHST0mdCF/vIhCPnG9vHQWe3WVjwIKANnuvD58ZAWR65n5ryA\nSOlCdjSXVWkkDoPWoC209fN5ikkodBpBocLTJIg1MGCUF7ThBCIxPTsvFwayuJ2G\nK1pp74P1S8SqtCr4fKGxhZSM9AyHDPSsQPhZSZg=\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIDdTCCAl2gAwIBAgILBAAAAAABFUtaw5QwDQYJKoZIhvcNAQEFBQAwVzELMAkG\nA1UEBhMCQkUxGTAXBgNVBAoTEEdsb2JhbFNpZ24gbnYtc2ExEDAOBgNVBAsTB1Jv\nb3QgQ0ExGzAZBgNVBAMTEkdsb2JhbFNpZ24gUm9vdCBDQTAeFw05ODA5MDExMjAw\nMDBaFw0yODAxMjgxMjAwMDBaMFcxCzAJBgNVBAYTAkJFMRkwFwYDVQQKExBHbG9i\nYWxTaWduIG52LXNhMRAwDgYDVQQLEwdSb290IENBMRswGQYDVQQDExJHbG9iYWxT\naWduIFJvb3QgQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDaDuaZ\njc6j40+Kfvvxi4Mla+pIH/EqsLmVEQS98GPR4mdmzxzdzxtIK+6NiY6arymAZavp\nxy0Sy6scTHAHoT0KMM0VjU/43dSMUBUc71DuxC73/OlS8pF94G3VNTCOXkNz8kHp\n1Wrjsok6Vjk4bwY8iGlbKk3Fp1S4bInMm/k8yuX9ifUSPJJ4ltbcdG6TRGHRjcdG\nsnUOhugZitVtbNV4FpWi6cgKOOvyJBNPc1STE4U6G7weNLWLBYy5d4ux2x8gkasJ\nU26Qzns3dLlwR5EiUWMWea6xrkEmCMgZK9FGqkjWZCrXgzT/LCrBbBlDSgeF59N8\n9iFo7+ryUp9/k5DPAgMBAAGjQjBAMA4GA1UdDwEB/wQEAwIBBjAPBgNVHRMBAf8E\nBTADAQH/MB0GA1UdDgQWBBRge2YaRQ2XyolQL30EzTSo//z9SzANBgkqhkiG9w0B\nAQUFAAOCAQEA1nPnfE920I2/7LqivjTFKDK1fPxsnCwrvQmeU79rXqoRSLblCKOz\nyj1hTdNGCbM+w6DjY1Ub8rrvrTnhQ7k4o+YviiY776BQVvnGCv04zcQLcFGUl5gE\n38NflNUVyRRBnMRddWQVDf9VMOyGj/8N7yy5Y0b2qvzfvGn9LhJIZJrglfCm7ymP\nAbEVtQwdpf5pLGkkeB6zpxxxYu7KyJesF12KwvhHhm4qxxYxldBniYUr+WymXUad\nDKqC5JlR3XC321Y9YeRq4VzW9v493kHMB65jUr9TU/Qr6cf9tveCX4XSQRjbgbME\nHMUfpIBvFSDJ3gyICh3WZlXi/EjJKSZp4A==\n-----END CERTIFICATE-----",
        "CertDomain": "*.weixin.qq.com",
        "CertSubjectDomain": [
            "*.weixin.qq.com",
            "*.cdn.myqcloud.com",
            "*.i.gtimg.cn",
            "*.imgcache.gtimg.cn",
            "*.imgcache.qq.com",
            "*.mail.qq.com",
            "*.mp.qq.com",
            "*.myapp.com",
            "*.qcloud.com",
            "*.qpic.cn",
            "*.qzonestyle.gtimg.cn",
            "*.qzs.qq.com",
            "*.tenpay.com",
            "*.url.cn",
            "*.weiyun.com",
            "*.wx.qq.com",
            "agame.qq.com",
            "cdn.b.qq.com",
            "combo.b.qq.com",
            "d3g.qq.com",
            "imgcache.qq.com",
            "music.qq.com",
            "pingjs.qq.com",
            "qzapp.qq.com",
            "rescdn.qqmail.com",
            "weiyun.com",
            "wximg.qq.com",
            "weixin.qq.com"
        ],
        "CertUploadTime": "2018-07-05 18:03:06",
        "CertBeginTime": "2018-03-08 11:21:27",
        "CertEndTime": "2019-03-09 11:21:27",
        "CertLoadBalancerSet": [
            {
                "LoadBalancerId": "lb-gdr96fc7",
                "LoadBalancerName": "5c1-LB",
                "VpcId": "vpc-muinpf9p",
                "RegionId": 4
            },
            {
                "LoadBalancerId": "lb-cegjj42t",
                "LoadBalancerName": "5e7-LB",
                "VpcId": "vpc-muinpf9p",
                "RegionId": 4
            }
        ],
        "RequestId": "e232cac4-b898-4a2a-9d66-31c02f63a89b"
    }
}
```

