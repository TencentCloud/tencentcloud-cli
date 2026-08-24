**Example 1: 查询证书列表示例**



Input: 

```
tccli tse DescribeCloudNativeAPIGatewayCertificates --cli-unfold-argument  \
    --GatewayId gateway-9a766f25 \
    --CertType SVR \
    --CertUsage CLIENT
```

Output: 
```
{
    "Response": {
        "Result": {
            "CertificatesList": [
                {
                    "BindDomains": [
                        "http-client-cert"
                    ],
                    "CertId": "ZVX5OKPW",
                    "CertSource": "ssl",
                    "CertType": "SVR",
                    "CertUsage": "CLIENT",
                    "CreateTime": "2026-07-26 17:21:04",
                    "Crt": "-----BEGIN CERTIFICATE-----\nMIIC8DCC**********IUOGzEBovJZBV00trHzcdiYdbLpKgwDQYJKoZIhvcNAQEL\nBQAwFjEUMBIGA1UEAwwLTUNQIFRlc3QgQ0EwHhcNMjYwNzI2MDkxMjA4WhcNMjcw\nNzI2MDkxMjA4WjAaMRgwFgYDVQ**************dC1jbGllbnQwggEiMA0GCSqG\nSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC+M8MTLWUcLIqtyOjk27luEK/DY6e0A4su\nPSHo9FVgeoNLOb11vP5RW***ple1sLCr8PhsZc*****************ZWjkGQtjY\nMwHZCSEfoWLfsCkmZACQcnCDgAUo7N0+vC5tgKIHyN/vAypG/gkpJGBnAHhME4vj\nEaW2kNussjZeqKZzYRG5PRVYUzigS+T6F6MNVUcMzImLRAovTOX1X7FuRW7fb+Qy\nRerjmgPv6gW9Tu1DNGpD1eSdTjbuGFmmazn8ar2zW4C7RzRMppoX9yM4AD0La9h5\nhtCuEta3K/YvFnUHJllKWeVKFO/TfaHMe18Mk8JZgkoMS3FuThGfAgMBAAGjMjAw\nMAkGA1UdEwQCMAAwDgYDVR0PAQH/BAQDAgeAMBMGA1UdJQQMMAoGCCsGAQUFBwMC\nMA0GCSqGSIb3DQEBCwUAA4IBAQAZTZGeKfhjzblh1/AJmKOQNWRz10Dumijh1cJz\nkwZXNA7GSE/dzwQhvcP8NifG8hWTpp0XnBqhHTTbeHjcwQmROxQYKC3UOFFqhKqA\nnGl4PRDFvG9RlTuIFzANgxCb5kIs82GF4RUMsH6uSz2U1bEoVEaN6JoaeIWnkcq+\nohqu3UpUa6s1zuV6bfbvr+VJ7eVhMYXcQ5td8v054zC/Scp94AHd02z+NlXCTRNm\nboibGeIxiQAmjaUlWglhQOTzzLB+ff8OyD2yUYzvC1JJjw7kEYJ6CDZ4LAMJ5Ht+\nHd8Q9McWGCb9s8FKJ/NUh1D5ay1NFUULjMl6ppeFLbNkQmqO\n-----END CERTIFICATE-----",
                    "ExpireTime": "2027-07-26 09:12:08",
                    "Id": "5cd6de2a-7a6c-40ea-bbdf-058ca6455411",
                    "IssueTime": "2026-07-26 09:12:08",
                    "Key": "-----BEGIN PRIVATE KEY-----\nMII*v******NBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAA**********TLWUcLIqt\nyOjk27luEK/DY6e0A4suPSHo9FVgeoNLOb11vP5RWoTnple1sLCr8PhsZcP5h6iT\nQCnC2SrPoCYZWjkGQtjYMwH************mZACQcnCDgAUo7N0+vC5tgKIHyN/v\nAypG/gkpJGBnAHhME4vjEaW2kNussjZeqKZzYRG5PRVYUzigS+T6F6MNVUcMzImL\nRAovTOX1X7FuR**********jmgPv6gW9Tu1DNGpD1eSdTjbuGFmmazn8ar2zW4C7\nRzRMppoX9yM4AD0La9h5htCuEta3K/YvFnUHJllKWeVKFO/TfaHMe18Mk8JZgkoM\nS3FuThGfAgMBAAECggEABLIedNDAGEv5OIUnSs8p6s+6pyZEs6sKup+DwM6XdQRR\nTYAlb0y1Mqj7cwSmUbQFCJmwaGyyw+xXexswbMETz4BysFmL4t2voNbRitww1ykS\n2dbtjScW5HoO0RBOEE6Yv73Bn653UZ3h+XKojowjCcL+Jkzaq3YoE/kRkEpPQhox\nW9ydn0DjuZ66LOgdA85DGf5v3u0hxl7syLSHfDVLavxwvSefKAtPg0sEGmnv3Ply\n+saha+wgcxSUZq7MGX4dRyrsgpgfFgL+5/78McDL7QByhd3HepokKz1TDtcUKFVw\nuBk3Hcgj4pSYJXRi9DIzkXpTrydhaX8lgHfg0TJvoQKBgQDfxJKQJoLW3V3yNdMx\noK3eBg3nkQl29kKwV6mxoulejglIc+NFm2fjhtrCmYLIJDbr5M8+CwzukLW57EIV\nEujD0gJdZ54r9Xi8JesyK9iMSXisUP7ipwkhEMIQc3MkampCXbOq3H8OQwMcwfx+\nCgsVEkq75ra3phkCpmx219g5VwKBgQDZmXUZzUME+8KwpDHhCduW5Jr/7/RdTIn7\nb4TMP6/ZojfCRziohwrrsGXfmTHFTYyApzIgGdjyfXwEM90s4r8gi0evuRb7umRc\n81v6arHxCuAA0hKLYUgDc+yTRLpvn7pB+POG7G6z+QX543Zcz0brE8JVEcJfDTEc\nbExDg+iU+QKBgASWw2qxX32IjKSq9enOocIr3Z0iHE+UPUngglpiPObzgr05oy+K\nQFcqLNJQ053HIFk2GAntsBY0YYWukqxb9uoNJH9F4LiGEDPLk0c0HvzBhPgDsTZ0\ntns3HMO5mmLky8kQot6eJvzj4ux0DfmHuzJzbZTs5lJd1aV4REErrAOBAoGAVc4o\nmhMR8X4hiKxGqvnLKJZe9Lu3fa733jlcgXo/qq9IE4koM3SE/umhUmnDcY0h8X18\ny6HFpeGLrNCSz+dd/MRPcWCoSn12pBym0XmPT4C9UjWEcIfc8Neem3gHmIrA1NEJ\nntPO15NEIwTqILDvwzUYdZk6L2cxTYb7D8iNR2kCgYARVeZT3/lu7cLJg1cLeK4Y\n9/cdJ3GJTHHtkU114f3NEeRVZJkfLYAt0+Ola39s+XxpFpqf3Mp3QEQqwX1g+R59\nUwMNP2oXP9/AixerJ8evl5i/p+EgLTVwrlrBdHlr1Z3DiFhruZguGIelTLGpkPzR\nJ0+2Vrhugba4esmxAsMcRA==\n-----END PRIVATE KEY-----",
                    "Name": "http-client-cert",
                    "ReferCount": 2,
                    "Status": "active"
                }
            ],
            "Pages": 1,
            "Total": 4
        },
        "RequestId": "3414649c-fcce-41e5-ad05-1f3356640713"
    }
}
```

