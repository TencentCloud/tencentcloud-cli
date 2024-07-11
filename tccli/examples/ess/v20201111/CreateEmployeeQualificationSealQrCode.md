**Example 1: 生成员工执业章授权二维码**

企业需要员工授权执业章使用权限给企业时，调用接口产生二维码

Input: 

```
tccli ess CreateEmployeeQualificationSealQrCode --cli-unfold-argument  \
    --Operator.UserId yDxVwUyKQWho8CUuO4zjEyQOAgwvr4Zy \
    --HintText 请授权执业章
```

Output: 
```
{
    "Response": {
        "QrcodeBase64": "/9ji1/Z**************/2Q==",
        "RequestId": "s1720524882444991481"
    }
}
```

