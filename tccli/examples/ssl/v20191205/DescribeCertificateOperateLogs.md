**Example 1: 获取用户近15天前5条证书操作日志**



Input: 

```
tccli ssl DescribeCertificateOperateLogs --cli-unfold-argument  \
    --Limit 5
```

Output: 
```
{
    "Response": {
        "AllTotal": 29,
        "TotalCount": 5,
        "OperateLogs": [
            {
                "Action": "用户[uin: 100017155920] 删除 证书[id: JiDVp1SG]",
                "CreatedOn": "2024-11-28 15:02:12",
                "Uin": "100017155920",
                "SubAccountUin": "100017155920",
                "CertId": "JiDVp1SG",
                "Type": "delete"
            },
            {
                "Action": "用户[uin: --]  证书[id: JiDVp1SG]",
                "CreatedOn": "2024-11-27 18:16:29",
                "Uin": "100017155920",
                "SubAccountUin": "--",
                "CertId": "JiDVp1SG",
                "Type": "revoked"
            },
            {
                "Action": "用户[uin: 100017155920] 吊销 证书[id: JiDVp1SG]",
                "CreatedOn": "2024-11-27 17:46:19",
                "Uin": "100017155920",
                "SubAccountUin": "100017155920",
                "CertId": "JiDVp1SG",
                "Type": "revoke"
            },
            {
                "Action": "用户[uin: --] 签发 证书[id: Juz8JAxn]",
                "CreatedOn": "2024-11-27 17:45:21",
                "Uin": "100017155920",
                "SubAccountUin": "--",
                "CertId": "Juz8JAxn",
                "Type": "issued"
            },
            {
                "Action": "用户[uin: --] 签发 证书[id: Juz9IaDi]",
                "CreatedOn": "2024-11-27 17:45:09",
                "Uin": "100017155920",
                "SubAccountUin": "--",
                "CertId": "Juz9IaDi",
                "Type": "issued"
            }
        ],
        "RequestId": "14727a68-3b90-4408-99c9-dea6d7de9456"
    }
}
```

