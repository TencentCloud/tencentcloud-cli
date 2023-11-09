**Example 1: 产品列表查询**

正常返回结果

Input: 

```
tccli weilingwith DescribeProductList --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --PageNumber 1 \
    --PageSize 1 \
    --ApplicationToken YzenL5LdGoxQM5gqJfCCoMDeGqUSsY78
```

Output: 
```
{
    "Response": {
        "RequestId": "8372d7e4-f04f-43bd-8f7d-d8b4586fdc8b",
        "Result": {
            "PageNumber": 1,
            "PageSize": 1,
            "Product": [
                {
                    "Attribute": 1,
                    "DeviceTypeId": "w777",
                    "DeviceTypeName": "",
                    "MaintenanceMfr": "未知厂商",
                    "Manufacturer": "未知厂商",
                    "ModelId": "",
                    "ModelName": "",
                    "ModelType": 0,
                    "ProductAbility": 1,
                    "ProductId": 2000051,
                    "ProductName": "视频网关",
                    "ProductType": "33",
                    "WorkspaceId": 1016
                }
            ],
            "TotalPage": 132,
            "TotalRow": 132
        }
    }
}
```

