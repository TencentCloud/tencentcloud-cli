**Example 1: 政策列表数据查询**

通过经销商政策code和产品二层名称查询政策列表数据

Input: 

```
tccli intlpartnersmgt QueryPolicyProductListByCode --cli-unfold-argument  \
    --PolicyCode StandardPolicy2024 \
    --ProductCode  \
    --ProductName  \
    --SubProductCode  \
    --SubProductName CBM Memory Optimized BMM5 \
    --Page 1 \
    --PageSize 200
```

Output: 
```
{
    "Response": {
        "ProductList": [
            {
                "ComponentCode": "*",
                "ComponentName": "*",
                "ComponentTypeCode": "*",
                "ComponentTypeName": "*",
                "EndDate": "2024-12-31 00:00:00",
                "PolicyCode": "StandardPolicy2024",
                "ProductCode": "p_cvm",
                "ProductName": "Cloud Virtual Machine(CVM)",
                "StartDate": "2024-01-01 00:00:00",
                "SubProductCode": "sp_cvm_bmm5m",
                "SubProductName": "CBM Memory Optimized BMM5"
            }
        ],
        "RequestId": "5d1eb9c4-8e1b-4c8c-99b3-209e7ce35a34",
        "Total": 55
    }
}
```

