**Example 1: 修改LDAP配置信息**

修改LDAP配置信息

Input: 

```
tccli bh ModifyLDAPSetting --cli-unfold-argument  \
    --Enable True \
    --Ip 192.168.***.** \
    --IpBackup 192.168.**.** \
    --Port 389 \
    --EnableSSL False \
    --BaseDN dc=my-domain,dc=com \
    --AdminAccount cn=Manager,dc=my-domain,dc=com \
    --AdminPassword ******** \
    --AttributeUser objectClass=organizationalPerson \
    --AttributeUserName cn \
    --AutoSync True \
    --Overwrite True \
    --SyncPeriod 30 \
    --SyncAll True \
    --SyncUnitSet ou=GGG,dc=my-domain,dc=com \
    --AttributeUnit objectClass=organizationalUnit \
    --AttributeRealName displayName \
    --AttributePhone mobile \
    --AttributeEmail mail \
    --DomainId net-6jvrhv6j \
    --ResourceId bh-saas-icgwc5mj
```

Output: 
```
{
    "Response": {
        "RequestId": "7a213e7a-53d2-45f7-94ba-60591b925e64"
    }
}
```

