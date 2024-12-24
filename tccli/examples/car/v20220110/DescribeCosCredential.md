**Example 1: 添加查询 COS 密钥信息请求**



Input: 

```
tccli car DescribeCosCredential --cli-unfold-argument  \
    --ApplicationId app-fcegkdfa \
    --ApplicationFileName xxx.rar
```

Output: 
```
{
    "Response": {
        "SecretID": "AKID_QiA9Vot9jsOFViCVxkg2ji_6CohydMxozhDBY7kGaYUD-kOFIBMT2xpxSxxx19m",
        "SecretKey": "XGSdS1K8lD6+qAPfQg6XSKrb1TgGEgPLdH62JeJgP0o=",
        "SessionToken": "OTyZlgQWTZKJ6jvOk3cvXQc91jCOLpGafb87702476f6cf4d23819b8d072de7320ze_i8PUZIIKEL9XVGO56mQzj0bLOs2J-qxuwYJ60-eCHKO7Gk-jaiQTZPql6ctGgfxnjNb8bnVw_-DS-DfOKFe8c0Q21roQFfiKYuBDwiIbh9-dZ0sXtE7qwcQKA-VEn_RrOBDonB9oa4lISOpapdmws4cKU0CpQTef4syDi2ixC-9CWnAcVveVSSgGLBKG7pGwBRX5Wx7BhtEQRdZnwvWdlqjunihHwxbi0KK1fEXjHa77MG5OPitJt_NxqTFm4sAJ4vSytHU-lNtFYzneTOkXvS191SlMC0sTcz25rhgxbRwZXjWa5NPI0daIrhcHaOY3qWBr2P2b-Ccda8NOHOdNnc7c9G85I76EBq9VGYU_mJj0qH6nARdhzXkzJ2Oq4Km_6_Awjyz_K3EqcS0r2kKzfEEo0lN0PduNlVfHlKRBi_NVDumIJAV-5Cvbt7wvJ6YAukG1Ea-rbMxZJY-WCyCkl1ExlcbYBT9ilm6rx6YHjuocJLSdozAtiS9uuGYCHiHrF3KADZlLNDomSRI1l1IB84GSaDe6Nkxc36B3z7aDewPA-OlFPJPKHKjLxGuQu2EcdvmJqhuq0E2MxtCbecL2le7yAjxZY0vi0iD56kNDlmWJ57cIM8bW2s03gGSN",
        "CosBucket": "application-test-1300543887",
        "CosRegion": "ap-guangzhou",
        "Path": "/1300055477/app-a1b2c3d4/ver-a1b2c3d4.zip",
        "StartTime": 1734950306,
        "ExpiredTime": 1734971906,
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022"
    }
}
```

