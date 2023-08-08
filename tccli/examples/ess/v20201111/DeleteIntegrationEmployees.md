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
                    "OpenId": "open123",
                    "Reason": "员工不存在",
                    "UserId": "ywksdfisjfks***023023df"
                }
            ],
            "SuccessEmployeeData": [
                {
                    "Mobile": "133*****1234",
                    "UserId": "ywklsjf*****9shdfdsk",
                    "DisplayName": "张*三"
                }
            ]
        },
        "RequestId": "s1290192***20323023"
    }
}
```

