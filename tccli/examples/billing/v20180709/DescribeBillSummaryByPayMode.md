**Example 1: Gets the bill summarized according to billing mode**



Input: 

```
tccli billing DescribeBillSummaryByPayMode --cli-unfold-argument  \
    --PayerUin 909619400 \
    --BeginTime '2018-11-01 00:00:00' \
    --EndTime '2018-11-01 23:59:59'
```

Output: 
```
{
  "Response": {
    "Ready": 1,
    "SummaryOverview": [
      {
        "PayMode": "prePay",
        "PayModeName": "Monthly subscription",
        “RealTotalCost": "0.00",
        "RealTotalCostRatio": "0.00",
        "Detail": []
      },
      {
        "PayMode": "postPay",
        "PayModeName": "Pay-as-you-go",
        “RealTotalCost": "440.66",
        "RealTotalCostRatio": "100.00",
        "Detail": [
          {
            "ActionType": "postpay_deduct",
            "ActionTypeName": "Pay-as-you-go deduction",
            “RealTotalCost": "441.25",
            "RealTotalCostRatio": "99.98"
          },
          {
            "ActionType": "offline_deduct",
            "ActionTypeName": "",
            “RealTotalCost": "0.10",
            "RealTotalCostRatio": "0.02"
          },
          {
            "ActionType": "billVirtualId",
            "ActionTypeName": "Monthly billing precision discrepancy",
            “RealTotalCost": "-0.69",
            "RealTotalCostRatio": "0.00"
          }
        ]
      }
    ],
    "RequestId": "59a408bc-5d95-4d40-bf21-58e5e8d48dd0"
  }
}
```

