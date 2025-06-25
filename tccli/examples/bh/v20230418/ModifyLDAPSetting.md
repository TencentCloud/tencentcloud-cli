**Example 1: 修改LDAP配置信息**

修改LDAP配置信息

Input: 

```
tccli bh ModifyLDAPSetting --cli-unfold-argument  \
    --Enable True \
    --AdminAccount admin \
    --AttributeEmail bhtets@email.com \
    --AdminPassword password \
    --AutoSync True \
    --Ip 172.168.0.1 \
    --BaseDN bhtest-dn \
    --SyncPeriod 1 \
    --SyncAll True \
    --EnableSSL True \
    --AttributeRealName attrRealName \
    --SyncUnitSet  \
    --IpBackup  \
    --AttributeUser user \
    --AttributeUserName testusername \
    --AttributePhone phone \
    --AttributeUnit unit \
    --Port 1 \
    --Overwrite True
```

Output: 
```
{
    "Response": {
        "RequestId": "9e5a83b7-564a-4831-8111-28a4ec740c61"
    }
}
```

