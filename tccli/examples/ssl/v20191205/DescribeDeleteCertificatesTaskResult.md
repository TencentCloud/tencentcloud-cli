**Example 1: 正常查询**

正常查询

Input: 

```
tccli ssl DescribeDeleteCertificatesTaskResult --cli-unfold-argument  \
    --TaskIds 11 12 13 15 14
```

Output: 
```
{
    "Response": {
        "DeleteTaskResult": [
            {
                "TaskId": "11",
                "Status": 0,
                "CertId": "1ODjBeH8",
                "Domains": [
                    "GMCert ECC Root CA - 01"
                ],
                "Error": null,
                "CacheTime": "2023-09-27 19:01:47"
            },
            {
                "TaskId": "12",
                "Status": 0,
                "CertId": "25EMBPYQ",
                "Domains": [
                    "hank.com"
                ],
                "Error": null,
                "CacheTime": "2023-09-27 19:01:48"
            },
            {
                "TaskId": "13",
                "Status": 0,
                "CertId": "txV0pewo",
                "Domains": [
                    "test.hankzzz.com"
                ],
                "Error": null,
                "CacheTime": "2023-09-27 19:01:48"
            },
            {
                "TaskId": "14",
                "Status": 4,
                "CertId": "rcGiGyTx",
                "Domains": [
                    "*.hath.fun"
                ],
                "Error": "有未解绑的云资源",
                "CacheTime": "2023-09-27 19:01:48"
            },
            {
                "TaskId": "15",
                "Status": 2,
                "CertId": "4FVmnb1u",
                "Domains": [
                    "*.hank-dv.com"
                ],
                "Error": "当前的证书状态不支持此操作",
                "CacheTime": "2023-09-27 19:01:48"
            }
        ],
        "RequestId": "037cc05f-c384-4d71-ab4f-a42d896ebb2e"
    }
}
```

