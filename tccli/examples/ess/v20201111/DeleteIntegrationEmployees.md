**Example 1: 删除员工（员工有待处理的合同）**

被删除员工存在待处理合同，且设置了交接人ReceiveUserId，调用此接口时，会先进行合同交接，然后删除员工。

Input: 

```
tccli ess DeleteIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId yDCNLUUckptelvkwUy06roXCPebdVqZt \
    --Employees.0.UserId yDCVKUUckpwsohygUEX7r4kvwy4jPAGW \
    --Employees.0.ReceiveUserId yDCNLUUckptelvkwUy06roXCPebdVqZt
```

Output: 
```
{
    "Response": {
        "DeleteEmployeeResult": {
            "SuccessEmployeeData": [
                {
                    "DisplayName": "典子谦",
                    "Mobile": "17300000000",
                    "UserId": "yDCVKUUckpwsohygUEX7r4kvwy4jPAGW"
                }
            ],
            "FailedEmployeeData": []
        },
        "RequestId": "f053ae01-9715-45e6-ad79-6d8a9a674fd7"
    }
}
```

**Example 2: 删除员工（员工没有待处理的合同）**

删除员工，不设置交接人（员工没有待处理的合同），员工将被直接移除。


Input: 

```
tccli ess DeleteIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId yDxbTUyKQWPt6NUuO4zjEuyFAyOX2v9C \
    --Employees.0.OpenId n9527
```

Output: 
```
{
    "Response": {
        "DeleteEmployeeResult": {
            "FailedEmployeeData": [],
            "SuccessEmployeeData": [
                {
                    "DisplayName": "张三",
                    "Mobile": "13500000000",
                    "UserId": "yDCNCUUckpv0ox66UC7yFOvFzax82lgp"
                }
            ]
        },
        "RequestId": "ee7969233c6c"
    }
}
```

**Example 3: 错误示例-如果没有设置交接人删除有处理合同的员工**

调用此接口时，若出现异常删除失败，员工信息及原因将会被返回。

Input: 

```
tccli ess DeleteIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId yDCNLUUckptelvkwUy06roXCPebdVqZt \
    --Employees.0.UserId yDCVKUUckpwsohygUEX7r4kvwy4jPAGW
```

Output: 
```
{
    "Response": {
        "DeleteEmployeeResult": {
            "SuccessEmployeeData": [],
            "FailedEmployeeData": [
                {
                    "UserId": "yDCVKUUckpwsohygUEX7r4kvwy4jPAGW",
                    "OpenId": "",
                    "Reason": "删除用户存在处理中的合同 ，需要指定交接人"
                }
            ]
        },
        "RequestId": "857544a1-9d6c-4304-8bf1-268163521060"
    }
}
```

