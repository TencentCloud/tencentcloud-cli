**Example 1: 创建员工-企微员工**

创建企微企业员工，只需传入WeworkOpenId参数即可。

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

**Example 2: 创建员工-非企微员工**

创建非企微企业的员工，传入必填参数即可。

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
                    "Mobile": "13545***901",
                    "Note": "",
                    "UserId": "*******"
                }
            ]
        },
        "RequestId": "s166*************073"
    }
}
```

**Example 3: 错误示例-入参不合法**

调用此接口时，需要按照入参描述进行相应的设置，以确保参数的合法性。如果参数设置不正确，会返回创建失败结果及原因。

Input: 

```
tccli ess CreateIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId y**********************************N \
    --Employees.0.DisplayName 张三（广东） \
    --Employees.0.Mobile 1***********7 \
    --Employees.0.OpenId open123
```

Output: 
```
{
    "Response": {
        "CreateEmployeeResult": {
            "FailedEmployeeData": [
                {
                    "DisplayName": "张三（广东）",
                    "Mobile": "1***********7",
                    "Reason": "参数错误,姓名不符合规范,请修改后重试",
                    "WeworkOpenId": ""
                }
            ],
            "SuccessEmployeeData": []
        },
        "RequestId": "s166*************073"
    }
}
```

