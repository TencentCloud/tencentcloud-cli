**Example 1: 获取人员到访**



Input: 

```
tccli chc DescribePersonnelVisitWorkOrderDetail --cli-unfold-argument  \
    --OrderId ord-25030712514742548
```

Output: 
```
{
    "Response": {
        "BaseInfo": {
            "EnterEndTime": "2025-03-21 00:00:00",
            "EnterStartTime": "2025-03-20 00:00:00",
            "IdcName": "天津数据备份中心东区3栋DC",
            "IdcUnitNameList": [
                "天津数据备份中心东区3栋DCM202"
            ],
            "VisitReason": [
                "OTHER"
            ],
            "VisitRemark": "test"
        },
        "OrderStatus": "processing",
        "PersonnelSet": [
            {
                "Company": "1",
                "Email": "",
                "IDCardNumber": "100000000000000005",
                "IDCardType": "IDENTITY_CARD",
                "LanguageType": "CHINESE",
                "Name": "1",
                "Position": "",
                "TelNumber": "13134567876",
                "Wechat": ""
            }
        ],
        "RequestId": "50904c59-ffef-4fef-b504-2c637f98906a",
        "StepSet": [
            {
                "FinishTime": "2025-03-07 12:51:47",
                "OwnerName": "zhangsan",
                "StepName": "发起申请",
                "StepStatus": "finish"
            },
            {
                "FinishTime": "",
                "OwnerName": "zhangsan",
                "StepName": "数经助理审批",
                "StepStatus": "processing"
            }
        ]
    }
}
```

