**Example 1: 测试LDAP连接**

测试LDAP连接

Input: 

```
tccli bh CheckLDAPConnection --cli-unfold-argument  \
    --Enable True \
    --Ip 192.168.***.** \
    --Port 389 \
    --EnableSSL False \
    --BaseDN dc=my-domain,dc=com \
    --AdminAccount cn=Manager,dc=my-domain,dc=com \
    --AdminPassword ******** \
    --IpBackup 192.168.**.** \
    --DomainId net-6jvrhv6j \
    --AttributeUserName cn \
    --ResourceId bh-saas-icgwc5mj
```

Output: 
```
{
    "Response": {
        "RequestId": "4f65a4eb-3b3f-494a-9c55-d758210d39d7"
    }
}
```

