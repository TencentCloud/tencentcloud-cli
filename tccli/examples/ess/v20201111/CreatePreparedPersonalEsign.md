**Example 1: 通过准备好的印章图片创建个人印章**

通过准备好的印章图片创建个人印章

Input: 

```
tccli ess CreatePreparedPersonalEsign --cli-unfold-argument  \
    --Operator.UserId abc \
    --UserName 印章归属个人姓名 \
    --IdCardType  \
    --IdCardNumber 身份证件号码 \
    --FileId yDxdfffxxxxxxxx \
    --SealName 我的印章名称 \
    --Mobile 135*111 \
    --EnableAutoSign True
```

Output: 
```
{
    "Response": {
        "SealId": "sealid-1",
        "RequestId": "abc"
    }
}
```

