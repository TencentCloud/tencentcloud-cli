**Example 1: 安装 SSL 证书**

安装 SSL 证书

Input: 

```
tccli lighthouse InstallCertificate --cli-unfold-argument  \
    --InstanceId lhins-aaaabbbb \
    --CertificateId yrrzyb53 \
    --Domain test.com
```

Output: 
```
{
    "Response": {
        "InvocationId": "inv-aaaaeeee",
        "RequestId": "cb31e424-0b5f-4f25-8cfc-76121aed5b58"
    }
}
```

