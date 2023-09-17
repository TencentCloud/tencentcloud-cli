**Example 1: 解除员工UserId与客户系统OpenId的绑定**

传入经过绑定的员工UserId与客户系统OpenId，调用此接口解绑成功，返回值Status为1。

Input: 

```
tccli ess UnbindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.UserId yDRCLUUXXXXXXXXXXXX4zjEwg0vjoimj \
    --UserId yDxVwUyXXXXXXXXXXXXjEyQOAgwvr4Zy \
    --OpenId open_user1
```

Output: 
```
{
    "Response": {
        "RequestId": "s16652185xxx032958",
        "Status": 1
    }
}
```

**Example 2: 错误示例-OpenId未经过绑定**

在调用此接口时，需确保OpenId已通过调用<a href="https://qian.tencent.com/developers/companyApis/staffs/BindEmployeeUserIdWithClientOpenId" target="_blank">BindEmployeeUserIdWithClientOpenId</a>接口与电子签系统的UserId绑定过。

Input: 

```
tccli ess UnbindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.UserId yDRCLUUXXXXXXXXXXXX4zjEwg0vjoimj \
    --UserId yDxVwUyXXXXXXXXXXXXjEyQOAgwvr4Zy \
    --OpenId 123
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "该openId并未绑定企业员工"
        },
        "RequestId": "dec22fb5-xxxx-xxxx-xxxx-xxxxxxc514d6"
    }
}
```

