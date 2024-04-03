**Example 1: 更新员工信息**

更新员工名称，手机号

Input: 

```
tccli ess UpdateIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --Employees.0.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --Employees.0.DisplayName 张三 \
    --Employees.0.Mobile 18888888888 \
    --Employees.0.Email zhangsan@qq.com
```

Output: 
```
{
    "Response": {
        "SuccessEmployeeData": [
            {
                "DisplayName": "张三",
                "Mobile": "18888888888",
                "UserId": "yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy"
            }
        ],
        "FailedEmployeeData": [],
        "RequestId": "s18mds3kjkld*****fssfsdfdsf"
    }
}
```

**Example 2: H5端修改未实名员工信息**

H5端,用户修改员工用户信息, 会生成一个链接,用户可通过这个链接,员工可通过此链接进入, 进行实名认证,加入企业

Input: 

```
tccli ess UpdateIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId yDxbTUyKQWPt6NUuO4zjEuyFAyOX2v9C \
    --Operator.ClientIp 8.8.8.8 \
    --InvitationNotifyType H5 \
    --JumpUrl https://www.qq.com \
    --Employees.0.UserId yDCNCUUckpv0ox66UC7yFOvFzax82lgp \
    --Employees.0.DisplayName dianziqian1 \
    --Employees.0.Mobile 13200000000
```

Output: 
```
{
    "Response": {
        "FailedEmployeeData": [],
        "RequestId": "s1705308707525950784",
        "SuccessEmployeeData": [
            {
                "DisplayName": "李四",
                "Mobile": "17612778521",
                "Url": "https://test.essurl.cn/TxHxUBCx0G",
                "UserId": "yDCNCUUckpv0ox66UC7yFOvFzax82lgp"
            }
        ]
    }
}
```

**Example 3: 错误示例：没有接口调用权限**

如果 Operator 里面的 UserId 没有对应的组织架构权限，则会报错没有 API 权限

Input: 

```
tccli ess UpdateIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId yDxbTUyKQWPt6NUuO4zjEuyFAyOX2v9C \
    --Operator.ClientIp 8.8.8.8 \
    --Employees.0.UserId yDCNCUUckpv0ox66UC7yFOvFzax82lgp \
    --Employees.0.DisplayName 李四 \
    --Employees.0.Mobile 15100000000
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied.NoApiAuth",
            "Message": "没有API权限"
        },
        "RequestId": "s2df9ddsk*****kfjdsklfjs"
    }
}
```

