**Example 1: 获取LDAP ou 列表**

获取LDAP ou 列表

Input: 

```
tccli bh DescribeLDAPUnitSet --cli-unfold-argument  \
    --Enable True \
    --Ip 192.168.***.** \
    --Port 389 \
    --EnableSSL False \
    --BaseDN dc=my-domain,dc=com \
    --AdminAccount cn=Manager,dc=my-domain,dc=com \
    --AdminPassword ******** \
    --AttributeUserName cn \
    --AttributeUnit objectClass=organizationalUnit \
    --IpBackup 192.168.**.** \
    --DomainId net-6jvrhv6j \
    --ResourceId bh-saas-icgwc5mj
```

Output: 
```
{
    "Response": {
        "UnitSet": [
            "ou=TTTT,dc=my-domain,dc=com"
        ],
        "RequestId": "7dabe376-93a2-42e1-8f37-6a7de78bb4cd"
    }
}
```

