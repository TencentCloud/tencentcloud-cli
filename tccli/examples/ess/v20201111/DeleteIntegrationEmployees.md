**Example 1: 删除员工**

删除员工，支持离职交接

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
            "FailedEmployeeData": [
                {
                    "OpenId": "SomeopenID",
                    "Reason": "员工不存在",
                    "UserId": "SomeUserID"
                }
            ],
            "SuccessEmployeeData": [
                {
                    "Mobile": "133XXXX1234",
                    "UserId": "SomeUserID",
                    "DisplayName": "SomeOne"
                }
            ]
        },
        "RequestId": "req123"
    }
}
```

