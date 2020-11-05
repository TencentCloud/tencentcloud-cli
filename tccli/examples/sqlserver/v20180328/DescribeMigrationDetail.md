**Example 1: Querying migration task details**



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
        "MigrateName": "Test API",
        "AppId": 1254065710,
        "Region": "ap-guangzhou",
        "SourceType": 5,
        "CreateTime": "2018-08-06 17:44:58",
        "StartTime": "0000-00- 00 00:00:00",
        "EndTime": "0000-00-00 00:00:00",
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
            "url": [
                "http://gz-oncvm-1254065710.cosgz.myqcloud.com/test4_20180724021516.bak",
                "http://gz-oncvm-1254065710.cosgz.myqcloud.com/testdb.bak"
            ],
            "urlPassword": ""
        },
        "Target": {
            "InstanceId ": "mssql-dr5843bdy",
            "UserName": "",
            "Password": ""
        },
        "MigrateDBSet": []
    }
}
```

