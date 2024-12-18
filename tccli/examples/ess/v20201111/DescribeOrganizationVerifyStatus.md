**Example 1: 查询当前企业在电子签的认证状态**

当前企业在电子签已经认证，企业调用方进行调用

Input: 

```
tccli ess DescribeOrganizationVerifyStatus --cli-unfold-argument  \
    --Operator.UserId yDRCLUUgygq2xun5UuO4zjEwg0vjoimj
```

Output: 
```
{
    "Response": {
        "RequestId": "49500cb4-ca5e-4da0-93fb-e15f3a710ed7",
        "VerifyStatus": 2
    }
}
```

