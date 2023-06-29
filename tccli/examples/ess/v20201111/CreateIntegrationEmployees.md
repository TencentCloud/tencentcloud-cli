**Example 1: 创建员工**

创建员工

Input: 

```
tccli ess CreateIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId y**********************************N \
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
        "RequestId": "s166*************073"
    }
}
```

