**Example 1: 删除员工**



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
                    "OpenId": "xx",
                    "Reason": "xx",
                    "UserId": "xx"
                }
            ],
            "SuccessEmployeeData": [
                {
                    "Mobile": "xx",
                    "UserId": "xx",
                    "DisplayName": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

