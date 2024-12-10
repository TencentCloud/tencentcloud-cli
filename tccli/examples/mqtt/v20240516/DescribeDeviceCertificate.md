**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeDeviceCertificate --cli-unfold-argument  \
    --DeviceCertificateSn 0eef68a582b94254296e54ce754f94d707a59911 \
    --InstanceId mqtt-jbgwp4ae
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "CaSn": "1b1e3bf3702110125887a3a721a7e66f05522513",
        "CertificateSource": "API",
        "ClientId": "111",
        "CreatedTime": 1724050379000,
        "DeviceCertificate": "-----BEGIN CERTIFICATE-----\nMIIEQjCCAyqgAwIBAgIUDu9opYK5QlQpblTOdU+U1welmREwDQYJKoZIhvcNAQEL\nBQAwgZIxCzAJBgNVBAYTAmNuMQ0wCwYDVQQIDAR4aWFuMQ0wCwYDVQQHDARodXlp\nMREwDwYDVQQKDAhqZWhhbnN1bjEWMBQGA1UECwwNdW5pdCBqZWhhbnN1bjEVMBMG\nA1UEAwwMc3Vuamlhbnhpb25nMSMwIQYJKoZIhvcNAQkBFhRqZWhhbnN1bkB0ZW5j\nZW50LmNvbTAeFw0yNDA1MDYwODU0NDNaFw0yNTA5MTgwODU0NDNaMIGBMQswCQYD\nVQQGEwJDTjELMAkGA1UECAwCWkoxCzAJBgNVBAcMAkhaMQwwCgYDVQQKDANBTEkx\nDTALBgNVBAsMBE1RVFQxFjAUBgkqhkiG9w0BCQEWB3h4eEB4eHgxIzAhBgNVBAMM\nGm1xdHQtdGVzdC54eHguYWxpeXVuY3MuY29tMIIBIjANBgkqhkiG9w0BAQEFAAOC\nAQ8AMIIBCgKCAQEArSMP1QFvggJVAth6Zhnf7NMWi+JP9TvnfzYl1xAWsWfX2ocN\nC+AumAQl7I0C2UMUppDHIRiikdAwqmoMLFkuTYCoPnTrk8FpQx+/bLXGNZzwgAKN\n8Y0dbEanl5y6UFXDB6ZsYhRJmjBEZoUj6xCeBzXxP2Uu0FPFAF5haLwt03gQMcWi\nEMHLdj/jFKUGoLns/eQUdE5wbsZjGrCmk5hEeJxa9vAw40W0cgwsVi0E8qt5FCj7\n11DeQsvZ5NlQVyOT6YOStElE2zuWtMjzsgk7ryW2qWANv62hRxY8dDmPXO5oimK8\nAzNjakiN40OmOhzwfiG3noItixlQywWppuTrfwIDAQABo4GeMIGbMB8GA1UdIwQY\nMBaAFEaWXAdZRRy3HPvjV6NBAYZYGhDfMAkGA1UdEwQCMAAwCwYDVR0PBAQDAgL0\nMEEGA1UdEQQ6MDiCEyoubXF0dC5hbGl5dW5jcy5jb22CIW1xdHQtdGVzdC5jbi1x\naW5nZGFvLmFsaXl1bmNzLmNvbTAdBgNVHQ4EFgQUz7CdvXCtki2X9i6zIQwKVJ7q\n/LwwDQYJKoZIhvcNAQELBQADggEBAB7Y/susqeC85RtXw9CHcOmcb/17G7svgxFZ\nLecOwEFxxaqwNVp/ae6TVkPvrMPStpVJmpS7ikYz37J16/n1mks/s+7fkGwAwfCI\nD+vGR+Hcvu2RsiTPwDMRhFwj92ZclnSyBjtPa1pgS1Nq0oCJ85G+nyxYBAjDQqzO\n05jNRO+E4/L+WrYhLE6M72amFMLbVGs170wHTiXtzokfUdflj9mNQs3pfLFNsyCt\nasDfqJX4Kie/MIwv/YKcB9pZ4NsonEgD3OfjJ6pFEHEH4ZiOVHuTT6C52XpCYMWA\najvuaaIlJp7GgOZxxPInOVXPmBlBlp28AiMlmxSfSAuMpUF0I8w=\n-----END CERTIFICATE-----\n",
        "DeviceCertificateCn": "mqtt-test.xxx.aliyuncs.com",
        "DeviceCertificateSn": "0eef68a582b94254296e54ce754f94d707a59911",
        "Format": "PEM",
        "LastActivationTime": 1724050378987,
        "LastInactivationTime": 0,
        "NotAfterTime": 1758185683000,
        "NotBeforeTime": 1714985683000,
        "RequestId": "1b5fc3fa-4bbf-421a-aad1-c45d49119a2c",
        "Status": "ACTIVE",
        "UpdateTime": 1724050379000
    }
}
```

