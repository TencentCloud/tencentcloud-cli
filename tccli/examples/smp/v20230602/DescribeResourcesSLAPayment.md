**Example 1: SLA赔付金额计算**

SLA赔付金额计算

Input: 

```
tccli smp DescribeResourcesSLAPayment --cli-unfold-argument  \
    --ProductCode p_cvm \
    --SubProductCode  \
    --PayerUin 客户UIN \
    --Operator abc \
    --Resources.0.ResourceId 资源ID \
    --Resources.0.DownMonth 2023-05 \
    --Resources.0.DownTime 10 \
    --Resources.0.ConsumptionBill.0.BusinessCode p_cvm \
    --Resources.0.ConsumptionBill.0.BusinessCodeName 云服务器CVM \
    --Resources.0.ConsumptionBill.0.CashPayAmount 7.71 \
    --Resources.0.ConsumptionBill.0.ConsumptionTypeName 续费分摊 \
    --Resources.0.ConsumptionBill.0.DailyTotalCost 0.72580645 \
    --Resources.0.ConsumptionBill.0.DayDiff 19 \
    --Resources.0.ConsumptionBill.0.FeeBeginTime 2023-05-13 00:00:00 \
    --Resources.0.ConsumptionBill.0.FeeEndTime 2023-05-31 23:59:59 \
    --Resources.0.ConsumptionBill.0.IncentivePayAmount 0.00000000 \
    --Resources.0.ConsumptionBill.0.OrderId 20230513400032203961682 \
    --Resources.0.ConsumptionBill.0.PayMode prePay \
    --Resources.0.ConsumptionBill.0.PayModeName 包年包月 \
    --Resources.0.ConsumptionBill.0.ProjectId 0 \
    --Resources.0.ConsumptionBill.0.ProjectName 默认项目 \
    --Resources.0.ConsumptionBill.0.RealCost 13.79 \
    --Resources.0.ConsumptionBill.0.RealTotalCost 7.71 \
    --Resources.0.ConsumptionBill.0.RegionId 1 \
    --Resources.0.ConsumptionBill.0.RegionName 华南地区（广州） \
    --Resources.0.ConsumptionBill.0.ResourceId 资源ID \
    --Resources.0.ConsumptionBill.0.ResourceName 未命名 \
    --Resources.0.ConsumptionBill.0.TransferPayAmount 0.00 \
    --Resources.0.ConsumptionBill.0.VoucherPayAmount 0.00000000 \
    --Resources.0.DeviceDealInfo.0.OrderId 20230513400032203961682 \
    --Resources.0.DeviceDealInfo.0.OrderData.UseBeginTime 2023-03-31 10:04:23 \
    --Resources.0.DeviceDealInfo.0.OrderData.UseEndTime 2024-03-31 23:59:59 \
    --Resources.0.DeviceDealInfo.0.OrderData.ResourceId 资源ID
```

Output: 
```
{
    "Response": {
        "RequestId": "dadcbddc-cc96-488d-b072-6de6bc713f00",
        "Data": {
            "PaymentInfos": [
                {
                    "PaymentResType": 1,
                    "ResourceId": "资源ID",
                    "PaymentAmount": 0.87,
                    "Availability": 95.448,
                    "PaymentRatio": 25,
                    "ExceptionMsg": ""
                }
            ],
            "PaymentAmountTotal": 0.87,
            "PaymentTraceId": "5ce2d8d5-5173-47a0-895d-4c0052d97f5f"
        }
    }
}
```

