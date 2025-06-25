**Example 1: 获取LDAP ou 列表**

获取LDAP ou 列表

Input: 

```
tccli bh DescribeLDAPUnitSet --cli-unfold-argument  \
    --Enable True \
    --AdminPassword pwd \
    --Ip 192.168.0.1 \
    --BaseDN bh-base-dn \
    --EnableSSL True \
    --IpBackup  \
    --AttributeUserName attr-user \
    --AdminAccount admin \
    --AttributeUnit attr-uint \
    --Port 22
```

Output: 
```
{
    "Response": {
        "UnitSet": [
            "bh-test-uint"
        ],
        "RequestId": "c7c79e35-65b9-4c2a-beea-a038fdf8c082"
    }
}
```

