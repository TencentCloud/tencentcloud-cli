**Example 1: 创建证书关联云资源异步任务**



Input: 

```
tccli ssl CreateCertificateBindResourceSyncTask --cli-unfold-argument  \
    --CertificateIds T****hh \
    --IsCache 1
```

Output: 
```
{
    "Response": {
        "CertTaskIds": [
            {
                "CertId": "T****hh",
                "TaskId": "7**99"
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

