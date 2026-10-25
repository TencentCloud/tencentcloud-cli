**Example 1: 请求示例**



Input: 

```
tccli iotexplorer DescribePrivateCA --cli-unfold-argument  \
    --CertName probe-upd-1022223352
```

Output: 
```
{
    "Response": {
        "CA": {
            "CertName": "probe-upd-1022223352",
            "CertSN": "21a8de82e8ca9ffffd40cef063bb900d46a4d45a",
            "CertText": "-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIUIajegujKn//9QM7wY7uQDUak1FowDQYJKoZIhvcNAQEL\nBQAwODELMAkGA1UEBhMCQ04xEjAQBgNVBAoMCUNhRTJFVGVzdDEVMBMGA1UEAwwM\nQ2FVcGRUZXN0LXYxMB4XDTI2MTAyMjE0MzM1MloXDTM2MTAxOTE0MzM1MlowODEL\nMAkGA1UEBhMCQ04xEjAQBgNVBAoMCUNhRTJFVGVzdDEVMBMGA1UEAwwMQ2FVcGRU\nZXN0LXYxMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvN/smQoAQIzU\ncKalHq014CLjF+FFh83meeUh5jKo8ok1DoO9JSwoSlwJNXRG01QygDiAC82rPbxs\neYnREZUBaTX2viHg2sdPkx9C5+UTPHZ+KclC4p5JlYxPn56aYSTeycRBOb6AGuyu\n3ijnsogwFCGLDNVc7zEwnWxzC3wiBJqQYvkClV53iU4ZIsvSuGADlRp6RN0jxMCg\nNMhj/F4AQ2/yH/6R+nWWaalSIsZ7Dze9+q+U7N0E4Nozr+GuD0AvMGP1X3LBp2Kh\ny6wbTur13gWcxAyNlWeJfX4hDRj78jPA7CMpQSWBK4uIbBDXlzQQT/kiieHzVjns\n9lckY06gjwIDAQABo3gwdjAdBgNVHQ4EFgQUE/iqcAaY73sASz1F2+PL35fIOxUw\nHwYDVR0jBBgwFoAUE/iqcAaY73sASz1F2+PL35fIOxUwDwYDVR0TAQH/BAUwAwEB\n/zAOBgNVHQ8BAf8EBAMCAQYwEwYDVR0lBAwwCgYIKwYBBQUHAwIwDQYJKoZIhvcN\nAQELBQADggEBAI9WVG1HsuZ0na3MdK+Mgyq+yt2xg7l2VU7GNReaOOHlTwsBVQlK\n5oOO/P89oD8PrXmaqMbv9N4eCv7SO49jr3rjmZGsAe5JNHIERZ49JPwlUH0TnQPk\nNMR2q7wslcLt7Zv3p5V2I9/WJIViwsidABVA4bXZYsF9SRuJCJMFMn4xuABHJFVD\nnHv7r+Dzya2fpJTJtOxwJ22Ek9j1T5av12rxbV5NsO7am5k+Zenp8I+rstBGoCSl\nWDXGBbICLnHUk2zN4iiDMrmaEjEYgUrC+7ahxiMQGKMfZaNxZiFYerJW3A2YvWdp\nbrzwbSh5zjBfeCzJxuEOfB6isqvwkVWbkic=\n-----END CERTIFICATE-----\n",
            "CreateTime": 1792679635,
            "EffectiveTime": 1792679632,
            "ExpireTime": 2108039632,
            "IssuerName": "CN=CaUpdTest-v1,O=CaE2ETest,C=CN",
            "Subject": "CN=CaUpdTest-v1,O=CaE2ETest,C=CN"
        },
        "RequestId": "abde230f-33e0-4a7c-b0b8-52cdf171f48a"
    }
}
```

