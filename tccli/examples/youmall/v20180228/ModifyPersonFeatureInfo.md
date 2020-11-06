**Example 1: 修改顾客特征信息**



Input: 

```
tccli youmall ModifyPersonFeatureInfo --cli-unfold-argument  \
    --CompanyId tencent \
    --ShopId 3030003 \
    --PersonId 3921 \
    --Picture picture \
    --PictureName picName \
    --PersonType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "83718397-3997-4e9f-b326-73a672697260",
        "CompanyId": "tencent",
        "ShopId": 3030003,
        "PersonId": 3921,
        "PersonIdBind": 3921,
        "PersonType": 1,
        "SimilarPersonIds": [
            3921
        ]
    }
}
```

