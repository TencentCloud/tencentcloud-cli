**Example 1: 批量创建用户**



Input: 

```
tccli tccatalog CreateUsers --cli-unfold-argument  \
    --Users.0.UserId 100008882712 \
    --Users.0.UserName Daniel \
    --Users.0.Source 2 \
    --Users.0.Description 测试用户 \
    --Users.0.RoleIds 1223 2254 \
    --Users.1.UserId 100008882713 \
    --Users.1.UserName Gain \
    --Users.1.Source 2 \
    --Users.1.RoleIds 4521
```

Output: 
```
{
    "Response": {
        "RequestId": "e634125c-b612-471a-90a2-d85a4e368ab2"
    }
}
```

