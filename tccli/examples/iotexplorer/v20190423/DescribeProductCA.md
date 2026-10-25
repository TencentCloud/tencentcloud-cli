**Example 1: 请求示例**



Input: 

```
tccli iotexplorer DescribeProductCA --cli-unfold-argument  \
    --ProductId SAGKS1EZQ2
```

Output: 
```
{
    "Response": {
        "CAs": [
            {
                "CertName": "e2e-ghost-ca-1020143925",
                "CertSN": "2806882401fe3864819d495da651e6e52e64567e",
                "CertText": "-----BEGIN CERTIFICATE-----\nMIIDiDCCAnCgAwIBAgIUKAaIJAH+OGSBnUldplHm5S5kVn4wDQYJKoZIhvcNAQEL\nBQAwQTELMAkGA1UEBhMCQ04xEjAQBgNVBAoMCUNhRTJFVGVzdDEeMBwGA1UEAwwV\nQ2FFMkVUZXN0VGhpcmRQYXJ0eUNBMB4XDTI2MTAyMDA2MzkyNVoXDTM2MTAxNzA2\nMzkyNVowQTELMAkGA1UEBhMCQ04xEjAQBgNVBAoMCUNhRTJFVGVzdDEeMBwGA1UE\nAwwVQ2FFMkVUZXN0VGhpcmRQYXJ0eUNBMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8A\nMIIBCgKCAQEAvcUC25CJb6Lb6z9LBYlY4CJg8Hpx8QloBbhG36rBo9Cr5v22cGd6\nQqFv3B+o4bo3lkKajyyCYSXF6JpdqWYBPl1KKMijml5EV6taMUzkh8T8J82OgZuX\npO2lIxoC3Pn8ySzuZ7BRjp0cUiKoWEM+3OVVeB84i6TprlxsovwUspknjkqIPHO0\nMN30m6mc4flqBYitj3rDo8YioAuyklmtK6BNHeu/SFiH2g6/0BdlefWbpLhiB0zz\nmTAykE9gTFJhaKnGVpOG43D1OwtBB8PkJBzu81wL6B+joMnPJ3GoJP31bL4MN02/\nyX+O9uJyMoziox+NixsVW5JiverZpWKyQQIDAQABo3gwdjAdBgNVHQ4EFgQUZZcw\nNDuQWD0BMrTpIF/GTH+kaQMwHwYDVR0jBBgwFoAUZZcwNDuQWD0BMrTpIF/GTH+k\naQMwDwYDVR0TAQH/BAUwAwEB/zAOBgNVHQ8BAf8EBAMCAQYwEwYDVR0lBAwwCgYI\nKwYBBQUHAwIwDQYJKoZIhvcNAQELBQADggEBALyrHmQaxSNTZIEA22v690lh9olt\nEGQs32FjAtzwd7mwsdc1t4E/USz6/trKBL6UUCEhQkSoL/b4PsLxsY5El45q8KvL\n8sfzKma1ycZMeSbZuY44m/XosgrdBivIxj1yDtFxFKSrhDR9dR2GMJskDQVyYeAF\nJZ2Slum57ZqzvaW7SAUF7T0cvgD3CnIWZhvsTtB6i8uEoFgJ7IfaFN+Ggm+SpBle\nu7cznyN7QD2x7j3Lk9iinhEk/w6qrWOBEw4u7WtwJzQIgfYd/2GgWchMOP7OCjDN\na6k2Nx1Kg2mRPy24f9dumwSFB8JJLBzTHbn/aWWwDKdv4Ww44hOCz5+xWlw=\n-----END CERTIFICATE-----\n",
                "CreateTime": 1792478367,
                "EffectiveTime": 1792478365,
                "ExpireTime": 2107838365,
                "IssuerName": "CN=CaE2ETestThirdPartyCA,O=CaE2ETest,C=CN",
                "Subject": "CN=CaE2ETestThirdPartyCA,O=CaE2ETest,C=CN"
            }
        ],
        "RequestId": "22da84d3-4928-47d1-9552-f4e8b142016f"
    }
}
```

