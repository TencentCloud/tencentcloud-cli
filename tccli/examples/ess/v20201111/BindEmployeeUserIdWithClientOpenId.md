**Example 1: 员工Userid与客户系统Openid绑定**

传入UserId和OpenId，绑定成功。

Input: 

```
tccli ess BindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.UserId yDRSRUUgygj6qnwfUuO4zjEwc193c2hH \
    --UserId yDRS4UUgygqdcj56UuO4zjExBQcOiB68 \
    --OpenId n9527
```

Output: 
```
{
    "Response": {
        "RequestId": "fc0b0a6b-01b4-4042-b236-c5356af1d5d8",
        "Status": 1
    }
}
```

**Example 2: 错误示例-重复使用OpenId绑定其他UserId**



Input: 

```
tccli ess BindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.UserId yDRSRUUgygj6qnwfUuO4zjEwc193c2hH \
    --UserId yDSLmUUckpou8bj8UyvAk4FBqAoWzvy4 \
    --OpenId n9527
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "该openid已绑定其他userid，请解绑后重试"
        },
        "RequestId": "535482ad-caa5-4302-909c-de054bf4df99"
    }
}
```

**Example 3: 错误示例-重复使用OpenId绑定同一个UserId**

接口绑定是不幂等的

Input: 

```
tccli ess BindEmployeeUserIdWithClientOpenId --cli-unfold-argument  \
    --Operator.UserId yDRSRUUgygj6qnwfUuO4zjEwc193c2hH \
    --UserId yDSLmUUckpou8bj8UyvAk4FBqAoWzvy4 \
    --OpenId n9527
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "该userId已绑定该openId，无需重新绑定"
        },
        "RequestId": "535482ad-caa5-4302-909c-de054bf4df99"
    }
}
```

