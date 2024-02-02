**Example 1: test**



Input: 

```
tccli emr DescribeUsersForUserManager --cli-unfold-argument  \
    --InstanceId emr-jnyiihlc \
    --UserManagerFilter.UserName sam \
    --PageSize 0 \
    --PageNo 0 \
    --NeedKeytabInfo True
```

Output: 
```
{
    "Response": {
        "RequestId": "782d3570-9f82-4bff-974a-17cf684fdfe9",
        "TotalCnt": 4,
        "UserManagerUserList": [
            {
                "CreateTime": "2022-05-12 17:40:23",
                "DownLoadKeyTabUrl": "",
                "SupportDownLoadKeyTab": true,
                "UserGroup": "test4",
                "UserName": "test4",
                "UserType": "NormalUser"
            },
            {
                "CreateTime": "2022-05-12 17:40:23",
                "DownLoadKeyTabUrl": "",
                "SupportDownLoadKeyTab": true,
                "UserGroup": "test3",
                "UserName": "test3",
                "UserType": "NormalUser"
            },
            {
                "CreateTime": "2022-05-12 17:40:23",
                "DownLoadKeyTabUrl": "https://cosulr/cluster/test2.keytab",
                "SupportDownLoadKeyTab": true,
                "UserGroup": "test2",
                "UserName": "test2",
                "UserType": "NormalUser"
            },
            {
                "CreateTime": "2022-05-12 17:40:23",
                "DownLoadKeyTabUrl": "https://cosulr/cluster/test1.keytab",
                "SupportDownLoadKeyTab": true,
                "UserGroup": "test1",
                "UserName": "test1",
                "UserType": "NormalUser"
            }
        ]
    }
}
```

