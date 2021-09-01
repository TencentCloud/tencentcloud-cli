**Example 1: 修改顾客身份类型接口-成功**



Input: 

```
tccli youmall ModifyPersonType --cli-unfold-argument  \
    --CompanyId testCompany1 \
    --ShopId 1 \
    --PersonId 1 \
    --PersonType 1 \
    --PersonSubType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6ec80684-0879-405e-8932-72e7c0c48ef8"
    }
}
```

**Example 2: 修改顾客身份类型接口-失败**



Input: 

```
tccli youmall ModifyPersonType --cli-unfold-argument  \
    --CompanyId testCompany1 \
    --ShopId 1 \
    --PersonId 1 \
    --PersonType 1 \
    --PersonSubType 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "Parameter CompanyId is missing"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

