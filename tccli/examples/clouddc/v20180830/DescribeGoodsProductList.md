**Example 1: 实例**

获取TCE产品列表

Input: 

```
tccli clouddc DescribeGoodsProductList --cli-unfold-argument  \
    --NeedDimension 1
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "IsCertificated": 0,
                "SubscriptionType": "xx",
                "Brief": "xx",
                "GoodsProperty": "xx",
                "DimensionGoodsProperty": "xx",
                "Channel": "xx",
                "BillOfMaterialList": [
                    {
                        "Remark": "xx",
                        "SaleMode": "xx",
                        "Name": "xx",
                        "GoodsId": 0,
                        "GoodsVersion": 0,
                        "MaterialList": [
                            {
                                "MaterialNum": "xx",
                                "MaterialVersion": 0,
                                "MaterialId": 0
                            }
                        ]
                    }
                ],
                "Status": 0,
                "IndustryTreeCd": "xx",
                "SubProductCode": "xx",
                "AssessmentLabel": "xx",
                "FeatureId": 0,
                "Price": [
                    {
                        "SaleMode": "xx",
                        "ControlDiscount": "xx",
                        "GmDiscount": "xx",
                        "PriceMode": "xx",
                        "LeaderDiscount": "xx",
                        "EndTime": "xx",
                        "PriceRatio": "xx",
                        "DiscountPrice": "xx",
                        "TaxRate": "xx",
                        "GoodsVersion": 0,
                        "Remark": "xx",
                        "PublishedPrice": "xx",
                        "LeaderLowPrice": "xx",
                        "ProfitRate": "xx",
                        "DirectorDiscount": "xx",
                        "GoodNumUnit": "xx",
                        "RelationGoodsId": "xx",
                        "GoodsId": 0,
                        "Cost": "xx",
                        "BeginTime": "xx",
                        "TimeUnit": "xx",
                        "DiscountLowPrice": "xx"
                    }
                ],
                "ChannelId": "xx",
                "BillingItemEnName": "xx",
                "ProductIncome": "xx",
                "GoodsLabel": "xx",
                "CostAggIdOne": 0,
                "GoodsVersion": 0,
                "CostAggIdThree": 0,
                "ChannelType": "xx",
                "ProductManagerOne": "xx",
                "SubBillingItemName": "xx",
                "PropertyId": "xx",
                "ProductCode": "xx",
                "BillingItemCode": "xx",
                "Name": "xx",
                "Cid": "xx",
                "IncomeDepartmentId": 0,
                "SubBillingItemEnName": "xx",
                "ProductManagerTwo": "xx",
                "SubProductEnName": "xx",
                "IncomeFeatureId": 0,
                "SalesIncome": "xx",
                "SubBillingItemCode": "xx",
                "DepartmentId": 0,
                "ProductOperationManager": "xx",
                "DeliveryTeam": "xx",
                "CloudType": 0,
                "ProductEnName": "xx",
                "SettGroupId": "xx",
                "SaleModes": "xx",
                "DimensionGoodsType": "xx",
                "IsLastVersion": 0,
                "Code": "xx",
                "IncomeGroupIdTwo": 0,
                "FinanceAssessLabel": "xx",
                "SettGroupName": "xx",
                "BillingItemName": "xx",
                "IncomeGroupIdOne": 0,
                "IsTmp": 0,
                "ProductName": "xx",
                "GoodsId": 0,
                "CostAggIdTwo": 0,
                "CostAggIdFour": 0,
                "SubProductName": "xx",
                "PropertyType": "xx",
                "ShortName": "xx",
                "GoodsType": "xx",
                "TmpStep": 0
            }
        ],
        "RequestId": "xx",
        "AllCount": 0
    }
}
```

