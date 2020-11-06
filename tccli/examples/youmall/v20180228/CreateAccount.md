**Example 1: 创建集团门店管理员账号-成功**



Input: 

```
tccli youmall CreateAccount --cli-unfold-argument  \
    --CompanyId "xx1" \
    --Name "135652123256" \
    --Password "1235$#1233" \
    --Remark "管理员张三" \
    --ShopCode "123"
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

**Example 2: 创建集团门店管理员账号-失败**



Input: 

```
tccli youmall CreateAccount --cli-unfold-argument  \
    --CompanyId "xx1" \
    --Name "1234" \
    --Password "1235$#1233" \
    --Remark "管理员张三" \
    --ShopCode "123"
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.InvalidParameter",
            "Message": "parameter is invalid"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

