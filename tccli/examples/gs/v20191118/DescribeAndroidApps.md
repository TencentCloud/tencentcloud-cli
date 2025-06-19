**Example 1: 查询安卓应用信息**

查询安卓应用信息

Input: 

```
tccli gs DescribeAndroidApps --cli-unfold-argument  \
    --Offset 2 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "Apps": [
            {
                "AndroidAppId": "apk-ne70ubtu",
                "AndroidAppVersionInfo": [
                    {
                        "AndroidAppVersion": "1705404913631168348",
                        "CreateTime": "2024-01-16T11:36:20Z",
                        "Command": "tar -zxvf test-1.0.X.tgz && cd test-1.0.X && ./install.sh",
                        "UninstallCommand": "cd test-1.0.X && ./uninstall.sh",
                        "CleanupMode": "CLEANUP_ON_UNINSTALL",
                        "State": "CREATE_SUCCESS",
                        "AndroidAppVersionName": "version_name"
                    },
                    {
                        "AndroidAppVersion": "1705406075397560877",
                        "CreateTime": "2024-01-16T11:54:35Z",
                        "Command": "tar -zxvf test-2.0.X.tgz && cd test-2.0.X && ./install.sh",
                        "UninstallCommand": "cd test-2.0.X && ./uninstall.sh",
                        "CleanupMode": "CLEANUP_AFTER_INSTALL",
                        "State": "CREATE_FAIL",
                        "AndroidAppVersionName": "version_name2"
                    }
                ],
                "Name": "test-app-1",
                "State": "ONLINE",
                "UserId": "user1",
                "AppMode": "ADVANCED",
                "CreateTime": "2024-01-16T11:54:35Z",
                "UpdateState": "CREATE_SUCCESS"
            },
            {
                "AndroidAppId": "apk-d6fyydrc",
                "AndroidAppVersionInfo": null,
                "Name": "test-app-2",
                "State": "ONLINE",
                "UserId": "user2",
                "AppMode": "NORMAL",
                "CreateTime": "2024-01-16T11:54:35Z",
                "UpdateState": "CREATE_SUCCESS"
            }
        ],
        "RequestId": "5eae7edb-7e12-451e-a4c1-7cf0b777c6e7",
        "TotalCount": 2
    }
}
```

