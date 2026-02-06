**Example 1: 查询单点登录企业员工信息**

查询单点登录员工账号信息
应用号：yDtrTUUckp94bix0UEbASLp1TuHxTYTS
OpenId： rUHYMgaz8aNm2IP3Pn8m5q6I3yJDojClFl555uLyeM0
当前 OpenId 还没有在腾讯电子签实名。

Input: 

```
tccli ess DescribeSingleSignOnEmployees --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvypUEfH3DjwIpMfa0uw \
    --Operator.ClientIp 8.8.8.8 \
    --SsoApplicationId yDtrTUUckp94bix0UEbASLp1TuHxTYTS \
    --OpenIds rUHYMgaz8aNm2IP3Pn8m5q6I3yJDojClFl555uLyeM0
```

Output: 
```
{
    "Response": {
        "Employees": [
            {
                "CreatedOn": 1758717608,
                "Email": "",
                "IsVerified": false,
                "Mobile": "138****8888",
                "Name": "典*谦",
                "OpenId": "rUHYMgaz8aNm2IP3Pn8m5q6I3yJDojClFl555uLyeM0",
                "RoleIds": [
                    "32bd40938602d1ee5f7735ee84af5785",
                    "yDCHgUUckpbubr9cUxrnpngClLR5YIkR"
                ],
                "UserId": ""
            }
        ],
        "RequestId": "s1758723951932552989"
    }
}
```

