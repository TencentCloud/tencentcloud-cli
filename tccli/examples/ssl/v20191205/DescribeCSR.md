**Example 1: 查询CSR**

查询CSR

Input: 

```
tccli ssl DescribeCSR --cli-unfold-argument  \
    --CSRId 12344
```

Output: 
```
{
    "Response": {
        "Id": 12344,
        "OwnerUin": "123",
        "Domain": "zz.zz.cn",
        "Organization": "yunzhi",
        "Department": "Light",
        "Email": "171008474@qq.com",
        "Province": "Hunan",
        "City": "changsha",
        "Country": "CN",
        "EncryptAlgo": "RSA",
        "KeyParameter": "2048",
        "Remarks": "",
        "Status": 1,
        "KeyPassword": "123abcccaa",
        "CreateTime": "2023-08-25 09:48:47",
        "CSR": "-----BEGIN CERTIFICATE REQUEST-----\r\nMIICnjCCAYYCAQAwWTEWMBQGA1UEAwwNenouSGF0aGxpbS5jbjEPMA0GA1UECgwG\r\neXVuemhpMREwDwYDVQQHDAhjaGFuZ3NoYTEOMAwGA1UECAwFSHVuYW4xCzAJBgNV\r\nBAYTAkNOMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAs8Wumn7cUG2d\r\n8ARiCg7rRtnNfonamdivha7bcm/xX4otKkI6f9TOjdO5TLQT2Qd55Iu8gVsGdFQ6\r\ntQwD/a3Koo2lD8XvBVI8R0LuGoK1jfChzglJo/FWwGyZjkMlUY6WisAk6utUYCSg\r\ncynZXDOkllEfwlkhsI4NbFG2ZrV7Ksj8Ed1e+Ki0GStVAb5j9qh/e4WeqE3IuZXG\r\ndofd/kEnvtprIasXgR+qpwwBTGpRwiqNhyP6z/xxM706eEhcnqh4oZi4abGCC2JM\r\nNJuVffFdmDiLaUKBrouk8WqZacB4nH1Uuk4y5eGGpxpX5UF+xgm/Sz0iI242dZFY\r\nDtqaSE8ZhwIDAQABoAAwDQYJKoZIhvcNAQEFBQADggEBAG8CES6epieMDaiXrEin\r\n2cVFxJUzrZf2aDm5YK4mAEz3h1kCQINDymtnQ4A4lFeQw+Le7xblS7qdMVT/5ecn\r\n64KbmfrThEaH/dTYOsbV7CipNfXiKH/SoD1Wz9bowNIxtXvy1t5Rlz3s8CBjKCKO\r\nj6vG+pUwh/mdAhpYlzh9VnfpMDAAtnBbxFhhLXqubiGe5YKqwuf3OwHov46g4+64\r\nPy8gmVbcqHy212Ea5wdOC+l54scm/b6bTdqo6Fv62bvepQI1mT5f198KTdKp1jCt\r\nw3gsfyY6WyL4zSvRgdbQyyWwys+rjsaNzqShSKxZ3xGKpdoOnK0uQX2RLfBB1nCi\r\nW9s=\r\n-----END CERTIFICATE REQUEST-----\r\n",
        "PrivateKey": null,
        "RequestId": "f00f136b-c0c8-476a-8097-b1bdfc9d330f"
    }
}
```

