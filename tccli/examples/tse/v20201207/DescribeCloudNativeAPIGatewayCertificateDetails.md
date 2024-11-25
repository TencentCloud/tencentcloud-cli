**Example 1: 查询云原生网关单个证书详情**

查询云原生网关单个证书详情

Input: 

```
tccli tse DescribeCloudNativeAPIGatewayCertificateDetails --cli-unfold-argument  \
    --GatewayId gateway-dde03767 \
    --Id ffadafb6-545d-461c-ad8c-baa26c0f8955
```

Output: 
```
{
    "Response": {
        "Result": {
            "Cert": {
                "Name": "tencent.com",
                "Id": "320c29fa-d5b1-425d-b701-91f213baf15c",
                "BindDomains": [
                    "tencent.com"
                ],
                "Status": "active",
                "Crt": "-----BEGIN CERTIFICATE-----\nMIICMjCCAZsCFCr/bVA0Qq2RMTTC7JYLPaHZA7+MMA0GCSqGSIb3DQEBCwUAMFgx\nCzAJBgNVBAYTAlhYMRUwEwYDVQQHDAxEZWZhdWx0IENpdHkxHDAaBgNVBAoME0Rl\nZmF1bHQgQ29tcGFueSBMdGQxFDASBgNVMAMMC3Rlc3R0cmUuY29tMB4XDTI0MDYx\nMjE2MDMzOFoXDTM0MDYxMDE2MDMzOFowWDELMAkGA1UEBhMCWFgxFTATBgNVBAcM\nDERlZmF1bHQgQ2l0eTEcMBoGA1UECgwTRGVmYXVsdCBDb21wYW55IEx0ZDEUMBIG\nA1UEAwwLdGVzdHRyZS5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBALSS\nn7JrfuasKBlrmGWFH6jxopQ2oVGbroX5nX5WD8BoK5a4Bv7RGk0i4ubw+9U8AGz9\nDfTOLedJW9a0bfZ33A6W64MSDpjvVbcsNV5XAm8b/MuWs86JmEpPVNwzqtghhbuR\nkoyWdUjzcqurqIqgkbNgDADI800rRbvpIsg0FwzbAgMBAAEwDQYJKoZIhvcNAQEL\nBQADgYEAQfSpNAmx1zdHF9x3kmX/+oZMgpzO/WWeuL//Lme+4GSrgsMHtI6Q3E9B\n4n2IeV3+89km6NeG6ZyJxTf/TBuP2NvR9sNbbAING9batYIzpRf8xe0QxEqdUEf6\nM6ECrHJPxKXm/as7RedPX4XKIaLDxshDvWFY2z7Ohv+Z/d82wV0=\n-----END CERTIFICATE-----",
                "Key": "-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQC0kp+ya37mrCgZa5hlhR+o8aKUNqFRm66F+Z1+Vg/AaCuWuAb+\n0RpNIuLm8PvVPABs/Q30zi3nSVvWtG32d9wOluuDEg6Y71W3LDVeWAJvG/zLlrPO\niZhKT1TcM6rYIYW7kZKMlnVI83Krq6iKoJGzYAwAyPNNK0W76SLINBcM2wIDAQAB\nAoGAbgP7SmBWA8KV987nHcs629rEnBqgtLDuZvALNaLHnAmbrQtYL75EkQSVS/E8\n7dDNzZlr/F/19blrO+fYK1chebb6yR5fRsb4yWacMwHf4ktAZbWuKlAo77kSnOkJ\nSX1d4fdqjUBLFkOF6A6YuO+fPJv0rxqjP7Xf/yFzcjA/C1kCQQDr2mIxKXUwVBQH\nffthb8Uau94DfmRhw3aglNBpuek4nbBEdA4LR/wQVsaqXB+U5F3FQzLEWHNTlAUk\nvPFoB6RVAkEAw/9f66uJ8SIj+BOOkqpBauqx/E4HKw+jpF/ZjS+GMENAE+t8zP53\n0fuqz+m+W/qAEoch8oJ8R84zHO9t+RecbwJBAN7/i+npxfjc9lcjIeS9tkKRsNfi\n0GyzUF2CdxAQDNhQGFKQ3JqEBGs6cPqwwdeYmKSj5cNJ0jkK8lYLI8F1wEUCQACj\nEte8Pf2Ho+BJh/wYC5CrnM+6HTHZoimFmjpoPiJoBY3LBqPP6+nFzJ9SXikEXmgx\nAj48iFTfabEdYhkeJ4cCQCbUEeZbxWvTAxjV3ALNlXDWUREJHnS7jlxXSTxzICLj\nd8inR2UhNvvlT033JZKkcbu47mqMmLpg40HcU/LlWlE=\n-----END RSA PRIVATE KEY-----\n",
                "ExpireTime": "2034-06-10 16:03:38",
                "CreateTime": "2024-06-13 00:05:51",
                "IssueTime": "2024-06-12 16:03:38",
                "CertSource": "ssl",
                "CertId": "FbRea1jX"
            }
        },
        "RequestId": "6bb87a9a-5656-4c5e-8bdf-b4c702991fc0"
    }
}
```

