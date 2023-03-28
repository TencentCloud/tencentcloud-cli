**Example 1: 更新员工信息**

更新员工名称，手机号

Input: 

```
tccli ess UpdateIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId abc \
    --Operator.Channel abc \
    --Operator.OpenId abc \
    --Operator.ClientIp abc \
    --Operator.ProxyIp abc \
    --Agent.AppId abc \
    --Agent.ProxyAppId abc \
    --Agent.ProxyOrganizationId abc \
    --Agent.ProxyOperator abc \
    --Employees.0.UserId abc \
    --Employees.0.DisplayName abc \
    --Employees.0.Mobile abc \
    --Employees.0.Email abc
```

Output: 
```
{
    "Response": {
        "SuccessEmployeeData": [
            {
                "DisplayName": "abc",
                "Mobile": "abc",
                "UserId": "abc"
            }
        ],
        "FailedEmployeeData": [],
        "RequestId": "abc"
    }
}
```

