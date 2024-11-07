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
                "AdminAccount": "admin",
                "AttributeEmail": "attr-email",
                "AutoSync": true,
                "Ip": "1.1.1.1",
                "BaseDN": "bh-test-dn",
                "SyncPeriod": 1,
                "SyncAll": true,
                "EnableSSL": true,
                "AttributeRealName": "attr-name",
                "SyncUnitSet": [
                    "uint"
                ],
                "IpBackup": "",
                "AttributeUser": "attr-user",
                "AttributeUserName": "attr-user-name",
                "AttributePhone": "attr-phone",
                "AttributeUnit": "attr-uint",
                "Port": 1,
                "Overwrite": true
            },
            "AuthMode": {
                "AuthMode": 1
            }
        },
        "RequestId": "dfac9070-8b23-499e-83b2-a50e3ca059af"
    }
}
```

