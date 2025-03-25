**Example 1: 创建服务器类型的设备型号评估工单**



Input: 

```
tccli chc CreateModelEvaluationWorkOrder --cli-unfold-argument  \
    --ModelSet.0.DevModel IBM X3650 M5 013 \
    --ModelSet.0.Version V1 \
    --CampusId 163 \
    --DeviceType server \
    --Remark 服务器型号评估
```

Output: 
```
{
    "Response": {
        "RequestId": "9bee9bdf-b631-414d-8d9b-20bdaddb87a2",
        "WorkOrderSet": [
            {
                "OrderType": "modelEvaluation",
                "ServiceType": "modelEvaluation",
                "WorkOrderId": "ord-25030711220788330"
            }
        ]
    }
}
```

