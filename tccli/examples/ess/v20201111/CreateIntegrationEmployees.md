**Example 1: H5端添加企业员工**

企业员工未认证， 在H5端， 用户通过生成链接嵌入到小程序，进行加入，实名

Input: 

```
tccli ess CreateIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvypUEfH3DjwIpMfa0uw \
    --Employees.0.DisplayName 典子谦 \
    --Employees.0.Mobile 13200000000 \
    --Employees.0.OpenId n9527 \
    --InvitationNotifyType H5 \
    --JumpUrl https://www.qq.com
```

Output: 
```
{
    "Response": {
        "CreateEmployeeResult": {
            "FailedEmployeeData": [],
            "SuccessEmployeeData": [
                {
                    "DisplayName": "典子谦",
                    "Mobile": "13200000000",
                    "Note": "",
                    "UserId": "yDCNCUUckpv0ox66UC7yFOvFzax82lgp",
                    "Url": "https://test.essurl.cn/TxHxUBCx0G",
                    "WeworkOpenId": ""
                }
            ]
        },
        "RequestId": "e01a9584-4b91-45dd-9a7b-46d32c4099fd"
    }
}
```

**Example 2: 创建员工-企微员工**

创建企微企业员工，只需传入WeworkOpenId参数即可。

Input: 

```
tccli ess CreateIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId yDwf3UUckps8dvypUEfH3DjwIpMfa0uw \
    --Employees.0.WeworkOpenId woed0SCQAAAtPx1SMU17ThB-QC7F
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
                    "UserId": "yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy",
                    "WeworkOpenId": "woed0SCQAAAtPx1SMU17ThB-QC7F"
                }
            ]
        },
        "RequestId": "s1695125479063466836"
    }
}
```

**Example 3: 创建员工-非企微员工**

创建非企微企业的员工，传入必填参数即可。

Input: 

```
tccli ess CreateIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId yyDxVwUyKQWho8CUuO4zjEyQOAgwvr4ZyN \
    --Employees.0.DisplayName 张三 \
    --Employees.0.Mobile 18560000000
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
                    "Mobile": "18560000000",
                    "Note": "",
                    "UserId": "yDRS4UUgygqdcjjhUuO4zjEBpXdcsHWw"
                }
            ]
        },
        "RequestId": "s1695125479063466836"
    }
}
```

**Example 4: 错误示例-入参不合法**

调用此接口时，需要按照入参描述进行相应的设置，以确保参数的合法性。如果参数设置不正确，会返回创建失败结果及原因。

Input: 

```
tccli ess CreateIntegrationEmployees --cli-unfold-argument  \
    --Operator.UserId yyDxVwUyKQWho8CUuO4zjEyQOAgwvr4ZyN \
    --Employees.0.DisplayName 张三（广东） \
    --Employees.0.Mobile 18560000000 \
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
                    "Mobile": "18560000000",
                    "Reason": "参数错误,姓名不符合规范,请修改后重试",
                    "WeworkOpenId": ""
                }
            ],
            "SuccessEmployeeData": []
        },
        "RequestId": "s1695125479063466836"
    }
}
```

