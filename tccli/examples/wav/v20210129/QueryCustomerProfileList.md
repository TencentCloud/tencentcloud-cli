**Example 1: 查询潜客客户存档信息**

用于查询潜客客户存档信息

Input: 

```
tccli wav QueryCustomerProfileList --cli-unfold-argument  \
    --Cursor 2Kgdu51quLaeNJSlwb79im883bftBE9d9Emju5I2MVw= \
    --Limit 100 \
    --BeginTime 1647187200 \
    --EndTime 1647273600
```

Output: 
```
{
    "Response": {
        "NextCursor": "2Kgdu51quLaeNJSlwb79im883bftBE9d9Emju5I2MVw=",
        "PageData": [
            {
                "CustomerId": 1234567890,
                "DealerCode": "abc",
                "UnionId": "ozynqsulJFCZ2z1aYeS8h",
                "CreateTime": "2023-01-01 00:00:00",
                "UserName": "张三",
                "Gender": 1,
                "Phone": "123****4567",
                "AgeRangeName": "26-30",
                "JobTypeName": "abc",
                "Address": "地址1",
                "LeadsProcessStatus": 0,
                "LeadType": 1,
                "SourceName": "自然到店",
                "LeadsLevelCode": "101",
                "VehicleBrandCode": "品牌编号",
                "VehicleSeriesCode": "车系编号",
                "VehicleTypeCode": "车型编号",
                "VehiclePurpose": {
                    "VehiclePurposeCode": "abc",
                    "VehiclePurposeName": "abc"
                },
                "PurchaseConcern": [
                    {
                        "Code": "abc",
                        "Description": "abc"
                    }
                ],
                "SalesName": "张三",
                "SalesPhone": "123****4567",
                "RealArrivalTime": 1618322621,
                "CompleteTestDriveTime": "2023-01-01 00:00:00",
                "OrderTime": 1618322621,
                "DeliveryTime": 1618322621,
                "InvoiceTime": 1618322621,
                "LoseTime": 1618322621,
                "CreatedAtTime": 1618322621,
                "ImportAtTime": 1618322621,
                "DistributeTime": 1618322621,
                "LeadCreateTime": 1618322621,
                "Nickname": "jack",
                "OrgIdList": [
                    "1"
                ],
                "Introducer": "李四",
                "IntroducerPhone": "123****4567",
                "FollowTime": 1618322621,
                "NextFollowTime": 1618322621,
                "EnterpriseTags": [
                    {
                        "GroupName": "标签分组名称",
                        "TagName": "标签名称",
                        "TagId": "etAJ2GCAAAXtWyujaWJHDDGi0mACHAAA"
                    }
                ],
                "ChannelTags": [
                    {
                        "TagName": "abc",
                        "TagId": "etAJ2GCAAAXtWyujaWJHDDGi0mACHAAA"
                    }
                ],
                "LeadId": 1348080105398452200,
                "WxId": "李四_1234",
                "Position": "销售",
                "IsBindWx": 1,
                "IsInvalid": 1,
                "InvalidType": "001",
                "InvalidTypeName": "无效",
                "InvalidTime": 1618322621,
                "InvalidRemark": "无效",
                "IsLose": 1,
                "LoseType": "001",
                "LoseTypeName": "战败",
                "LoseRemark": "战败"
            }
        ],
        "RequestId": "fea177dd-9fa6-4e76-9c8f-67f5a21f20bb"
    }
}
```

