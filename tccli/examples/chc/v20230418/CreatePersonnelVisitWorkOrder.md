**Example 1: 创建人员到访工单**



Input: 

```
tccli chc CreatePersonnelVisitWorkOrder --cli-unfold-argument  \
    --PersonnelSet.0.IDCardNumber **** \
    --PersonnelSet.0.IDCardType IDENTITY_CARD \
    --PersonnelSet.0.Company 某某公司 \
    --PersonnelSet.0.LanguageType CHINESE \
    --PersonnelSet.0.Name 张三 \
    --PersonnelSet.0.TelNumber 13800138000 \
    --PersonnelSet.0.Position 工程师 \
    --PersonnelSet.0.Wechat zhangsan_wechat \
    --PersonnelSet.0.Email zhangsan@example.com \
    --IdcId 373 \
    --IdcUnitIdSet 2555 \
    --EnterStartTime 2025-03-08 17:25:04 \
    --EnterEndTime 2025-03-10 17:25:04 \
    --VisitReason IT_OPERATION \
    --VisitRemark 需要参观
```

Output: 
```
{
    "Response": {
        "RequestId": "289288d7-d662-4b66-b4ef-d18d8913ca18",
        "WorkOrderSet": [
            {
                "OrderType": "personnelVisit",
                "ServiceType": "personnelVisit",
                "WorkOrderId": "ord-25030711303576000"
            }
        ]
    }
}
```

