**Example 1: 查询产品的CA证书**



Input: 

```
tccli iotcloud DescribeProductCA --cli-unfold-argument  \
    --ProductId ABCDE12345
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxxxxxxxxxxx",
        "CAs": [
            {
                "CreateTime": 1622619674,
                "EffectiveTime": 1622448592,
                "ExpireTime": 1653984592,
                "CertText": "-----BEGIN CERTIFICATE-----\nMIIDgTCCAmmgAwIBAgIUX/aeTIr85dbejTlbNGcpRPW0dlowDQYJKoZIhvcNAQEL\nBQAwUDELMAkGA1UEBhMCQ04xEjAQBgNVBAgMCWd1YW5nZG9uZzERMA8GA1UEBwwI\nc2hlbnpoZW4xDDAKBgNVBAoMA0FBQTEMMAoGA1UEAwwDQUFBMB4XDTIxMDUzMTA4\nMDk1MloXDTIyMDUzMTA4MDk1MlowUDELMAkGA1UEBhMCQ04xEjAQBgNVBAgMCWd1\nYW5nZG9uZzERMA8GA1UEBwwIc2hlbnpoZW4xDDAKBgNVBAoMA0FBQTEMMAoGA1UE\nAwwDQUFBMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA65Rt1X/RBdG6\n24JYIJrsYOC8NALr/i7jA13v3EHEOjA2505G3YM7RL/NeHIMD7m3XYH2lqHv9XVU\nHzd+stK5MXXmVSIazt2BYaTdIzWOl0sPQGU9BaIloZyb1nSR/UAZ7sJpon5+nTvV\nNUUnkVC36BgWUKfLOTlmKkzlHOLecD/WAzgIJ55NC6QsjKWiKXBm5mtlz4uoZ7Bh\nhQGM/8Zax1YLYnMwkQrMB/o8ma/o5/wRpdqKT0ixm2yZMxW3c6XHGpEioowbJnHa\nH4AZm8LAVIH+TtGZoeKRppTfEArlszocuxZHTfk5XJZh0NsofmwKm4BPmMzW+9tF\nRvEwnnES1QIDAQABo1MwUTAdBgNVHQ4EFgQU0wRl/eNy5y9eF1xcJlosQoyTAHsw\nHwYDVR0jBBgwFoAU0wRl/eNy5y9eF1xcJlosQoyTAHswDwYDVR0TAQH/BAUwAwEB\n/zANBgkqhkiG9w0BAQsFAAOCAQEAO9P5UH8If1Qb/Za4M1gwCylIVtexON7qOk5Y\nqWlPvhG+fpqeA/fJQq/3LnKbL2b8Dm/SUFEUAsZs/MptXC5d7E++MwDaiVVQ5rNy\nemHpNrgHXoPZ9JdB4plFWF4K8CvIcLEmlyG6tj9mBbQ/toBqHpGdkaGTQMP/UjxQ\nbZFrV9YiRodEQHfEXD5ZXwvt3VZsfIbz8gf+flAanx8Ce1EeaZDbQZuqbRHt4FKS\nJoasx3KICfdGocM6PGA7smAYc7MFszAS4tGS9H75EZqNZdseKsct9vP3TCb4hE5x\nupDam8V9w/SQ9vMGzeW1FM91BfWuRXgsv/Bz4FQdeV1+Xyf+Eg==\n-----END CERTIFICATE-----",
                "CertName": "XKFAWDE6LX",
                "CertSN": "5ff69e4c8afce5d6de8d395b34672944f5b4765a",
                "IssuerName": "CN=AAA,O=AAA,L=shenzhen,ST=guangdong,C=CN",
                "Subject": "CN=AAA,O=AAA,L=shenzhen,ST=guangdong,C=CN"
            }
        ]
    }
}
```

