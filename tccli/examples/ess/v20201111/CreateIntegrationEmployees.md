**Example 1: 创建员工**



Input: 

```
tccli ess CreateIntegrationEmployees --cli-unfold-argument  \
    --Operator.ProxyIp  \
    --Operator.ClientIp 0.0.0.1 \
    --Operator.UserId y**********************************N \
    --Operator.Channel  \
    --Operator.OpenId  \
    --Employees.0.DisplayName 张三 \
    --Employees.0.Mobile 12345678901 \
    --Employees.0.OpenId open123
```

Output: 
```
{
    "Response": {
        "CreateEmployeeResult": {
            "FailedEmployeeData": [],
            "SuccessEmployeeData": [
                {
                    "DisplayName": "张三",
                    "Mobile": "1***********7",
                    "UserId": "*******"
                }
            ]
        },
        "RequestId": "s1663585682405723073"
    }
}
```

