**Example 1: 查询安全配置信息**

查询安全配置信息

Input: 

```
tccli bh DescribeSecuritySetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "SecuritySetting": {
            "Login": {
                "LockTime": 1,
                "LockThreshold": 1,
                "TimeOut": 1
            },
            "Password": {
                "MinLength": 1,
                "Complexity": 1,
                "CheckHistory": 1,
                "ValidTerm": 1
            },
            "LDAP": {
                "Enable": true,
                "AdminAccount": "root",
                "AttributeEmail": "1297**@qq.com",
                "AutoSync": true,
                "Ip": "127.0.0.1",
                "BaseDN": "dn",
                "SyncPeriod": 1,
                "SyncAll": true,
                "EnableSSL": true,
                "AttributeRealName": "zhangsan",
                "SyncUnitSet": [
                    ""
                ],
                "IpBackup": "127.0.0.1",
                "AttributeUser": "zhangsan",
                "AttributeUserName": "test-name",
                "AttributePhone": "138*****",
                "AttributeUnit": "unit",
                "Port": 1,
                "Overwrite": true
            },
            "AuthMode": {
                "AuthMode": 1
            }
        },
        "RequestId": "b8ebf0b3-ecf5-49bf-9f9d-86341c4072f1"
    }
}
```

