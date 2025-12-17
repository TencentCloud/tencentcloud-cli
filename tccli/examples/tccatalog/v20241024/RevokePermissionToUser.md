**Example 1: 用户解绑权限**



Input: 

```
tccli tccatalog RevokePermissionToUser --cli-unfold-argument  \
    --UserId 700002180075 \
    --SecurableObjects.0.FullName layyu_c2.default \
    --SecurableObjects.0.Type SCHEMA \
    --SecurableObjects.0.Privileges.0.Name GRANT_PRIVILEGES \
    --SecurableObjects.0.Privileges.0.Condition ALLOW
```

Output: 
```
{
    "Response": {
        "RequestId": "c1222cee-73a1-4831-be1d-2d595838bd41"
    }
}
```

