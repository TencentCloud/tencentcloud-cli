**Example 1: 创建一个单点登录的员工成功示例**

创建单点登录员工账号成功
应用号：yDtrTUUckp94bix0UEbASLp1TuHxTYTS
OpenId：OpenId [rUHYMgaz8aNm2IP3Pn8m5q6I3yJDojClFl555uLyeM0] 
姓名：电子签
手机号：18888888888
角色：合同管理员和印章管理员的 roleId

Input: 

```
tccli ess CreateSingleSignOnEmployees --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvypUEfH3DjwIpMfa0uw \
    --Operator.ClientIp 8.8.8.8 \
    --SsoApplicationId yDtrTUUckp94bix0UEbASLp1TuHxTYTS \
    --Employees.0.OpenId rUHYMgaz8aNm2IP3Pn8m5q6I3yJDojClFl555uLyeM0 \
    --Employees.0.Name 典子谦 \
    --Employees.0.Mobile 18888888888 \
    --Employees.0.RoleIds 32bd40938602d1ee5f7735ee84af5785 yDCHgUUckpbubr9cUxrnpngClLR5YIkR
```

Output: 
```
{
    "Response": {
        "ErrorMessages": [
            ""
        ],
        "RequestId": "s1758723146173417020",
        "Status": 0
    }
}
```

**Example 2: 创建一个单点登录的员工失败示例**

创建单点登录员工账号失败
应用号：yDtrTUUckp94bix0UEbASLp1TuHxTYTS
原因：OpenId [rUHYMgaz8aNm2IP3Pn8m5q6I3yJDojClFl555uLyeM0] 已存在于系统中
建议：请检查当前员工是否已经导入，如果确定没有被导入使用其他OpenId。

Input: 

```
tccli ess CreateSingleSignOnEmployees --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvypUEfH3DjwIpMfa0uw \
    --Operator.ClientIp 8.8.8.8 \
    --SsoApplicationId yDtrTUUckp94bix0UEbASLp1TuHxTYTS \
    --Employees.0.OpenId rUHYMgaz8aNm2IP3Pn8m5q6I3yJDojClFl555uLyeM0 \
    --Employees.0.Name 典子谦 \
    --Employees.0.Mobile 18888888888 \
    --Employees.0.RoleIds 32bd40938602d1ee5f7735ee84af5785 yDCHgUUckpbubr9cUxrnpngClLR5YIkR
```

Output: 
```
{
    "Response": {
        "ErrorMessages": [
            "导入员工失败，错误信息:[当前openId[rUHYMgaz8aNm2IP3Pn8m5q6I3yJDojClFl555uLyeM0]已经被绑定了，请更换openId进行绑定]"
        ],
        "RequestId": "s1758723146173417020",
        "Status": 2
    }
}
```

