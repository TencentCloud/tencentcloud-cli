**Example 1: 创建证书关联云资源异步任务**



Input: 

```
tccli ssl CreateCertificateBindResourceSyncTask --cli-unfold-argument  \
    --CertificateIds abc \
    --IsCache 1
```

Output: 
```
{
    "Response": {
        "CertTaskIds": [
            {
                "CertId": "abc",
                "TaskId": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

