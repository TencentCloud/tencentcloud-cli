**Example 1: 创建访问凭证**

创建访问凭证

Input: 

```
tccli cfs CreateAccessCert --cli-unfold-argument  \
    --CertDesc test
```

Output: 
```
{
    "Response": {
        "RequestId": "fjo8aejo-fjei-32eu-2je9-fhue83nd81",
        "CertId": "cfscert-1234abcd"
    }
}
```

