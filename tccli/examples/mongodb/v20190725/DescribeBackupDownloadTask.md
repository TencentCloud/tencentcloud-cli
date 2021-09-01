**Example 1: 查询备份下载任务**



Input: 

```
tccli mongodb DescribeBackupDownloadTask --cli-unfold-argument  \
    --InstanceId cmgo-dygv1rnp \
    --Status 2
```

Output: 
```
{
    "Response": {
        "RequestId": "c41c0c46-7d5a-49b9-832a-557880c1e9ef",
        "Tasks": [
            {
                "BackupName": "cmgo-dygv1rnp_2021-03-26 10:44",
                "BackupSize": 844,
                "CreateTime": "2021-03-26 10:47:37",
                "Percent": 100,
                "ReplicaSetId": "cmgo-dygv1rnp_0",
                "Status": 2,
                "TimeSpend": 0,
                "Url": "https://mognodb-backup-test-tar-1251937656.cos.ap-guangzhou.myqcloud.com/cmgo-dygv1rnp_2021-03-26%2010%3A44%2Fcmgo-dygv1rnp_0.tar?q-sign-algorithm=sha1&q-ak=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&q-sign-time=1616726859%3B1616813259&q-key-time=1616726859%3B1616813259&q-header-list=host&q-url-param-list=&q-signature=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
            }
        ],
        "TotalCount": 1
    }
}
```

