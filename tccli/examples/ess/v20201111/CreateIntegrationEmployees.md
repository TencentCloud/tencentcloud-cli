**Example 1: 创建企微员工**

创建企微员工

Input: 

```
tccli ess CreateIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId y**********************************N \
    --Employees.0.WeworkOpenId f****f
```

Output: 
```
{
    "Response": {
        "CreateEmployeeResult": {
            "FailedEmployeeData": [],
            "SuccessEmployeeData": [
                {
                    "DisplayName": "",
                    "Mobile": "",
                    "Note": "",
                    "UserId": "yDRGJ******wG5veA",
                    "WeworkOpenId": "f****f"
                }
            ]
        },
        "RequestId": "s166*************073"
    }
}
```

**Example 2: 创建 非企微员工**

创建非企微员工

Input: 

```
tccli ess CreateIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId y**********************************N \
    --Employees.0.DisplayName 张三 \
    --Employees.0.Mobile 13545***901 \
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
                    "Note": "",
                    "UserId": "*******"
                }
            ]
        },
        "RequestId": "s166*************073"
    }
}
```

