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
    --Resources.0.DownTime 10
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
            "PaymentAmountTotal": 0.87
        }
    }
}
```

