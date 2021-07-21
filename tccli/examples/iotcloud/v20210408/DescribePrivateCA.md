**Example 1: 查询私有化CA证书信息**



Input: 

```
tccli iotcloud DescribePrivateCA --cli-unfold-argument  \
    --CertName testuuu
```

Output: 
```
{
    "Response": {
        "CA": {
            "EffectiveTime": 1623210302,
            "ExpireTime": 1654746302,
            "CertText": "-----BEGIN CERTIFICATE-----\r\nMIIC3DCCAcSgAwIBAgIBATANBgkqhkiG9w0BAQsFADAWMRQwEgYDVQQDDAtAMTYy\r\nMzIxMDMwMjAeFw0yMTA2MDkwMzQ1MDJaFw0yMjA2MDkwMzQ1MDJaMBYxFDASBgNV\r\nBAMMC0AxNjIzMjEwMzAyMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA\r\n4+iCByP5dpVPBEO3Fa6kvBTPZEMqcyPNrGl9sJOuX5v2sXy6BYbI4dxiRbLdkiqu\r\nOM/aUR+cY1/yA9NjtMsx7B1R7nNvuT4j2pZQfQ214HeGLuSFiw1OPYDKAlaBoG+x\r\nNWnEnTo2F2rNXddQ69tIciCLtqqP6CcO3F63/l6uGMhsR1QEQbdVG2+CjRYRO0Bf\r\nPPDyWT0W/CocVRBvnfMF7vNUpD+Nw7QcgKwaCzokvuUfBYRmRC5ah1FGktp7An+A\r\neQ4Vg948lzRKlYJB2CYTAp8TQqI+h2G8wHXT//5d220KrLa+tQqnu6+4iufrBYm4\r\nc1tLOJaBQguUSyJv6/+cgQIDAQABozUwMzATBgNVHSUEDDAKBggrBgEFBQcDAjAP\r\nBgNVHRMBAf8EBTADAQH/MAsGA1UdEQQEMAKCADANBgkqhkiG9w0BAQsFAAOCAQEA\r\njZFx2FsxlvJotM10mCD2AkXOxGqIqy1KZcKxtF5ayDRERV1crvgnIHzpTX+pziRa\r\nAC1zAXbuudVnhBgeIA2Hkm1Q1f3QeIWZsSABtV2WZt5YQ1JJ1fkqi22lF+SsxG5g\r\n/vJnI00YYYEdeoj4Bp5OOTolRIfZ0rnfNzGt+CDcG02dC7qgdoVis/Rw1GYOC/h+\r\nLBN7xhM+ctEqLmiQSgmSqEfHgU2GB32ULdyCxWN91ywsg8VWsXo+bDkdpxhPbCuF\r\nziI6ef/JWtym4mkpdFjVjISaE7oaWm5gMLdcGi0G/Gysetil71QMHmacQvrrjMI4\r\nhsqtDwSvAU75hKKYSyTRdQ==\r\n-----END CERTIFICATE-----\r\n",
            "CertName": "testuuu",
            "CertSN": "1",
            "IssuerName": "CN=@1623210302",
            "Subject": "CN=@1623210302",
            "CreateTime": 1623833012
        },
        "RequestId": "xxxxxx"
    }
}
```

