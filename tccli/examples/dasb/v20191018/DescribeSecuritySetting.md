**Example 1: 查询安全配置信息**

查询安全配置信息

Input: 

```
tccli dasb DescribeSecuritySetting --cli-unfold-argument ```

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
                "AdminAccount": "xx",
                "AttributeEmail": "xx",
                "AutoSync": true,
                "Ip": "xx",
                "BaseDN": "xx",
                "SyncPeriod": 1,
                "SyncAll": true,
                "EnableSSL": true,
                "AttributeRealName": "xx",
                "SyncUnitSet": [
                    "xx"
                ],
                "IpBackup": "xx",
                "AttributeUser": "xx",
                "AttributeUserName": "xx",
                "AttributePhone": "xx",
                "AttributeUnit": "xx",
                "Port": 1,
                "Overwrite": true
            },
            "AuthMode": {
                "AuthMode": 1
            }
        },
        "RequestId": "xx"
    }
}
```

