**Example 1: 更换用户组**



Input: 

```
tccli tccatalog ModifyUsersOfGroupSTD --cli-unfold-argument  \
    --Group test_create \
    --Users 700002180075 \
    --OperateAction ADD \
    --UserType Cam
```

Output: 
```
{
    "Response": {
        "RequestId": "a982eea6-05db-462f-bf26-b329ca708c3c"
    }
}
```

