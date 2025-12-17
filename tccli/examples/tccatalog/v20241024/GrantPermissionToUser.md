**Example 1: 用户授予权限**



Input: 

```
tccli tccatalog GrantPermissionToUser --cli-unfold-argument  \
    --UserId 700002180075 \
    --SecurableObjects.0.FullName layyu_lakehouse.s1 \
    --SecurableObjects.0.Type SCHEMA \
    --SecurableObjects.0.Privileges.0.Name USE_SCHEMA \
    --SecurableObjects.0.Privileges.0.Condition ALLOW
```

Output: 
```
{
    "Response": {
        "RequestId": "b9f3a087-0874-4068-9c01-76cb45c05ad3"
    }
}
```

