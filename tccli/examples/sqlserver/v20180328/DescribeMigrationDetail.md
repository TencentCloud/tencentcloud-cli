**Example 1: 查询迁移任务详情**



Input: 

```
tccli sqlserver DescribeMigrationDetail --cli-unfold-argument  \
    --MigrateId 2728
```

Output: 
```
{
    "Response": {
        "RequestId": "4be5990d-a4b5-49dc-b2b4-e713b6aa7ba3",
        "MigrateId": 2728,
        "MigrateName": "测试接口",
        "AppId": 1254065710,
        "Region": "ap-guangzhou",
        "SourceType": 5,
        "CreateTime": "2018-08-06 17:44:58",
        "StartTime": "2020-09-22 00:00:00",
        "EndTime": "2020-09-22 00:00:00",
        "Status": 1,
        "Progress": 0,
        "MigrateType": 2,
        "Source": {
            "InstanceId": "",
            "CvmId": "",
            "VpcId": "",
            "SubnetId": "",
            "UserName": "",
            "Password": "",
            "Ip": "",
            "Port": 0,
            "Url": [
                "http://gz-oncvm-1254065710.cosgz.myqcloud.com/test4_20180724021516.bak",
                "http://gz-oncvm-1254065710.cosgz.myqcloud.com/testdb.bak"
            ],
            "UrlPassword": ""
        },
        "Target": {
            "InstanceId": "mssql-dr5843bdy",
            "UserName": "",
            "Password": ""
        },
        "MigrateDBSet": []
    }
}
```

