**Example 1: 创建审计日志文件**



Input: 

```
tccli cynosdb DescribeAuditLogFiles --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-qwerasdf
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "TotalCount": 1,
        "Items": [
            {
                "Status": "creating",
                "FileName": "audit_log_file",
                "DownloadUrl": "https://gz-audit-1256375829.cos.ap-guangzhou.myqcloud.com/183367353_cdb-j0skeo3t_1694001004_7113542.csv?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKID3rhYBaa9HVeKkvpd072tVt2x2khNYopc%26q-sign-time%3D1694001006%3B1694087406%26q-key-time%3D1694001006%3B1694087406%26q-header-list%3D%26q-url-param-list%3D%26q-signature%3Dbb41113d6e580050730d492886b59d730a474764",
                "FileSize": 123,
                "CreateTime": "2019-03-20 17:09:13",
                "ErrMsg": ""
            }
        ]
    }
}
```

