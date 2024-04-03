**Example 1: 错误示例-OpenId未经过绑定**

在调用此接口时，需确保OpenId已通过调用<a href="https://qian.tencent.com/developers/companyApis/staffs/BindEmployeeUserIdWithClientOpenId" target="_blank">BindEmployeeUserIdWithClientOpenId</a>接口与电子签系统的UserId绑定过。

Input: 

```
tccli ess UnbindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.UserId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --UserId yDwJ0UUckpk2077eUxgm9jJv5GGyJXCh \
    --OpenId n9527
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "该openId并未绑定企业员工"
        },
        "RequestId": "s1615674603446404796"
    }
}
```

**Example 2: 解除员工UserId与客户系统OpenId的绑定**

传入经过绑定的员工UserId与客户系统OpenId，调用此接口解绑成功，返回值Status为1。

Input: 

```
tccli ess UnbindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.UserId yDRS4UUgygqdcj2tUuO4zjEEFuP35Swc \
    --UserId yDxbNUyKQDxGYNUuO4zjEwvl3XYQmAcO \
    --OpenId n9527
```

Output: 
```
{
    "Response": {
        "RequestId": "s1665674603446404796",
        "Status": 1
    }
}
```

