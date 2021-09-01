**Example 1: 删除顾客特征-成功**



Input: 

```
tccli youmall DeletePersonFeature --cli-unfold-argument  \
    --CompanyId TestCompany \
    --ShopId 1 \
    --PersonId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

**Example 2: 删除顾客特征-失败**



Input: 

```
tccli youmall DeletePersonFeature --cli-unfold-argument  \
    --CompanyId TestCompany \
    --ShopId 1 \
    --PersonId 1
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "Parameter ShopId is missing"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

