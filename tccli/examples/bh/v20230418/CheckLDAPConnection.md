**Example 1: 测试LDAP连接**

测试LDAP连接

Input: 

```
tccli bh CheckLDAPConnection --cli-unfold-argument  \
    --Enable True \
    --AdminPassword pwd \
    --Ip 10.10.1.10 \
    --BaseDN bh-test-DN \
    --EnableSSL True \
    --IpBackup  \
    --AdminAccount admin \
    --Port 80
```

Output: 
```
{
    "Response": {
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082"
    }
}
```

