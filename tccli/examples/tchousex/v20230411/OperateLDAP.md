**Example 1: 检查ldap连接**



Input: 

```
tccli tchousex OperateLDAP --cli-unfold-argument  \
    --ApiType CheckLdapConnection \
    --InstanceCheck 1 \
    --InstanceId instance-yud3owzz \
    --LdapConfig.LdapBaseDn dc=example,dc=com \
    --LdapConfig.LdapBindDn cn=admin,dc=example,dc=com \
    --LdapConfig.LdapBindPasswd /N7xXdT+7cW7DA7eqgsMxQ== \
    --LdapConfig.LdapUrl ldap://9.0.8.12:389 \
    --LdapConfig.LdapUserFilter cn \
    --LdapConfig.ServerCa -----BEGIN CERTIFICATE----- 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 -----END CERTIFICATE----- \
    --LdapConfig.VerifyClientCa True \
    --LdapConfig.VerifyServerCa True
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "API request failed: Instance is not exist",
        "ReturnData": "",
        "RequestId": "e6e9b9a9-dfae-4c62-aae7-2b5438e4be6e"
    }
}
```

