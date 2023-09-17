**Example 1: 删除员工**

删除员工，不设置交接人，员工将被直接移除。


Input: 

```
tccli ess DeleteIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId y**********************************N \
    --Employees.0.OpenId open123
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
                    "UserId": "yDRt******************BKpnZs"
                }
            ]
        },
        "RequestId": "ee79xxxx-xxxx-xxxx-xxxx-xxxx69233c6c"
    }
}
```

**Example 2: 删除员工，并设置交接人**

被删除员工存在待处理合同，且设置了交接人ReceiveUserId，调用此接口时，会先进行合同交接，然后删除员工。

Input: 

```
tccli ess DeleteIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId yDxb******************MHc55R \
    --Employees.0.OpenId open123 \
    --Employees.0.ReceiveUserId yDRC******************vjoimj
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
                    "UserId": "yDRt******************BKpnZs"
                }
            ]
        },
        "RequestId": "ee79xxxx-xxxx-xxxx-xxxx-xxxx69233c6c"
    }
}
```

**Example 3: 错误示例-员工不属于当前企业**

调用此接口时，若出现异常删除失败，员工信息及原因将会被返回。

Input: 

```
tccli ess DeleteIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId yDxb******************MHc55R \
    --Employees.0.UserId yDRt******************BKpnZs
```

Output: 
```
{
    "Response": {
        "DeleteEmployeeResult": {
            "FailedEmployeeData": [
                {
                    "OpenId": "",
                    "Reason": "员工不属于当前企业",
                    "UserId": "yDRt******************BKpnZs"
                }
            ],
            "SuccessEmployeeData": []
        },
        "RequestId": "ee79xxxx-xxxx-xxxx-xxxx-xxxx69233c6c"
    }
}
```

