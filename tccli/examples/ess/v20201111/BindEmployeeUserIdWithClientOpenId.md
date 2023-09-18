**Example 1: 员工Userid与客户系统Openid绑定**

传入UserId和OpenId，绑定成功。

Input: 

```
tccli ess BindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.UserId yDwgKUUcXXXXXXXXXXXXXXXXXXQxx2u1 \
    --UserId yDwgKUUcXXXXXXXXXXXXXXXXXXQZDRuD \
    --OpenId open_user2
```

Output: 
```
{
    "Response": {
        "RequestId": "s1665xxxxx74024539",
        "Status": 1
    }
}
```

**Example 2: 错误示例-重复绑定**

调用此接口时，请确保用户ID参数未经过绑定，否则接口将返回错误信息。以传入UserId已绑定为例，接口提示不需重新绑定。

Input: 

```
tccli ess BindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.UserId yDwgKUUcXXXXXXXXXXXXXXXXXXQxx2u1 \
    --UserId yDwgKUUcXXXXXXXXXXXXXXXXXXQZDRuD \
    --OpenId open_user2
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "该userId已绑定该openId，无需重新绑定"
        },
        "RequestId": "5116xxxx-xxxx-xxxx-xxxx-xxxx5f02877b"
    }
}
```

