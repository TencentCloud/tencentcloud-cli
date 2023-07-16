**Example 1: 查询单库备份的明细**

查询单库备份的明细

Input: 

```
tccli sqlserver DescribeBackupFiles --cli-unfold-argument  \
    --Limit 20 \
    --Offset 0 \
    --InstanceId mssql-mz23h8n7 \
    --GroupId 241259
```

Output: 
```
{
    "Response": {
        "BackupFiles": [
            {
                "CrossBackupAddr": [
                    {
                        "CrossExternalAddr": "https://sqlserver-bucket-sg-1258415541.cos.ap-singapore.myqcloud.com/1251966477%2fsqlserver%2fmssql-mz23h8n7%2fbackup%2fmanual_specific_58002_db2_2021_09_14144312.bak?sign=q-sign-algorithm%3dsha1%26q-ak%3dAKIDrRloa5Zdk580Xo9dCWaNE3kU3MQElsiV%26q-sign-time%3d1631605556%3b1631606456%26q-key-time%3d1631605556%3b1631606456%26q-header-list%3d%26q-url-param-list%3d%26q-signature%3df977b8f1afee59225e41a9e766b035953ef9527c",
                        "CrossInternalAddr": "https://sqlserver-bucket-sg-1258415541.cos.ap-singapore.myqcloud.com/1251966477%2fsqlserver%2fmssql-mz23h8n7%2fbackup%2fmanual_specific_58002_db2_2021_09_14144312.bak?sign=q-sign-algorithm%3dsha1%26q-ak%3dAKIDrRloa5Zdk580Xo9dCWaNE3kU3MQElsiV%26q-sign-time%3d1631605556%3b1631606456%26q-key-time%3d1631605556%3b1631606456%26q-header-list%3d%26q-url-param-list%3d%26q-signature%3df977b8f1afee59225e41a9e766b035953ef9527c",
                        "CrossRegion": "ap-singapore"
                    }
                ],
                "Region": "ap-singapore",
                "DBs": [
                    "db1"
                ],
                "DownloadLink": "https://sqlserver-bucket-sg-1258415541.cos.ap-singapore.myqcloud.com/1251966477%2fsqlserver%2fmssql-mz23h8n7%2fbackup%2fmanual_specific_58002_db1_2021_09_14144312.bak?sign=q-sign-algorithm%3dsha1%26q-ak%3dAKIDrRloa5Zdk580Xo9dCWaNE3kU3MQElsiV%26q-sign-time%3d1631605556%3b1631606456%26q-key-time%3d1631605556%3b1631606456%26q-header-list%3d%26q-url-param-list%3d%26q-signature%3de5e61bfbccf44f6c3dd8a710296108dc95ba16db",
                "FileName": "manual_specific_58002_db1_2021_09_14144312.bak",
                "Id": 36074,
                "Size": 184
            }
        ],
        "RequestId": "cb2fb9fa-152f-11ec-ac75-525400542aa6",
        "TotalCount": 2
    }
}
```

