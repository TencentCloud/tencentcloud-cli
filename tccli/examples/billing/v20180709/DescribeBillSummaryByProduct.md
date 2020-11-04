**Example 1: 获取产品汇总费用分布**



Input: 

```
tccli billing DescribeBillSummaryByProduct --cli-unfold-argument  \
    --PayerUin 909619400\
    --BeginTime '2018-11-01 00:00:00'\
    --EndTime '2018-11-01 23:59:59'
```

Output: 
```
{
    "Response": {
        "Ready": 1,
        "SummaryTotal": {
            "RealTotalCost": "1596.49",
            "VoucherPayAmount": "176.00",
            "IncentivePayAmount": "0.00",
            "CashPayAmount": "1420.49"
        },
        "SummaryOverview": [
            {
                "BusinessCode": "p_cvm",
                "RealTotalCost": "540.00",
                "CashPayAmount": "540.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "33.77",
                "BillMonth": "2018-11",
                "BusinessCodeName": "云服务器CVM"
            },
            {
                "BusinessCode": "p_cbs",
                "RealTotalCost": "536.54",
                "CashPayAmount": "536.54",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "33.57",
                "BillMonth": "2018-11",
                "BusinessCodeName": "云硬盘CBS"
            },
            {
                "BusinessCode": "p_cos",
                "RealTotalCost": "219.44",
                "CashPayAmount": "219.44",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "13.73",
                "BillMonth": "2018-11",
                "BusinessCodeName": "COS 对象存储"
            },
            {
                "BusinessCode": "p_ai_image_ocr",
                "RealTotalCost": "169.83",
                "CashPayAmount": "0.01",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "169.82",
                "RealTotalCostRatio": "10.62",
                "BillMonth": "2018-11",
                "BusinessCodeName": "OCR文字识别"
            },
            {
                "BusinessCode": "p_yunjing",
                "RealTotalCost": "81.00",
                "CashPayAmount": "81.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "5.07",
                "BillMonth": "2018-11",
                "BusinessCodeName": "云镜（主机安全）"
            },
            {
                "BusinessCode": "p_blackstone_eip",
                "RealTotalCost": "45.00",
                "CashPayAmount": "45.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "2.82",
                "BillMonth": "2018-11",
                "BusinessCodeName": "黑石弹性公网IP"
            },
            {
                "BusinessCode": "p_ai_image",
                "RealTotalCost": "4.78",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "4.78",
                "RealTotalCostRatio": "0.30",
                "BillMonth": "2018-11",
                "BusinessCodeName": "图像识别"
            },
            {
                "BusinessCode": "p_ai_image_facerecognize",
                "RealTotalCost": "1.39",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "1.39",
                "RealTotalCostRatio": "0.09",
                "BillMonth": "2018-11",
                "BusinessCodeName": "人脸识别"
            },
            {
                "BusinessCode": "p_cdn",
                "RealTotalCost": "0.46",
                "CashPayAmount": "0.46",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.03",
                "BillMonth": "2018-11",
                "BusinessCodeName": "内容分发网络CDN"
            },
            {
                "BusinessCode": "p_ci",
                "RealTotalCost": "0.00",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "BusinessCodeName": "数据万象CI"
            },
            {
                "BusinessCode": "p_cmq",
                "RealTotalCost": "0.00",
                "CashPayAmount": "0.00",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.00",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "BusinessCodeName": "消息服务CMQ"
            },
            {
                "BusinessCode": "billVirtualId",
                "RealTotalCost": "-1.95",
                "CashPayAmount": "-1.96",
                "IncentivePayAmount": "0.00",
                "VoucherPayAmount": "0.01",
                "RealTotalCostRatio": "0.00",
                "BillMonth": "2018-11",
                "BusinessCodeName": "月度计费精度差异"
            }
        ],
        "RequestId": "8a57841e-ef77-413d-a8ba-4c607173663c"
    }
}
```

