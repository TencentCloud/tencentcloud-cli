**Example 1: 查看个人自动签开启状态**

查看个人自动签开启状态

Input: 

```
tccli ess DescribeUserAutoSignStatus --cli-unfold-argument  \
    --Operator.UserId abc \
    --SceneKey E_PRESCRIPTION_AUTO_SIGN \
    --UserInfo.Name 小明 \
    --UserInfo.IdCardNumber 610000000000000000 \
    --UserInfo.IdCardType ID_CARD
```

Output: 
```
{
    "Response": {
        "IsOpen": true,
        "LicenseFrom": 1684412179,
        "LicenseTo": 1715948179,
        "RequestId": "5beb5fxxxxx-a97c85196a3e"
    }
}
```

