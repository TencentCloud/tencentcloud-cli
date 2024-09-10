**Example 1: 获取代金券使用记录**

获取代金券使用记录

Input: 

```
tccli billing DescribeVoucherUsageDetails --cli-unfold-argument  \
    --Limit 10 \
    --Offset 1 \
    --VoucherId "abc" \
    --Operator "abc"
```

Output: 
```
{
    "Response": {
        "RequestId": "9168e8fe-ed79-4726-9ced-29033e5a7011",
        "TotalCount": 5,
        "TotalUsedAmount": 5000000,
        "UsageRecords": [
            {
                "PayMode": "prepay",
                "PayScene": "",
                "SeqId": "20240212840001259973831114",
                "UsageDetails": [
                    {
                        "Action": "purchase",
                        "BillingItemCode": "",
                        "CalcUnit": "",
                        "ProductCode": "p_cvm",
                        "ProductEnName": "Cloud Virtual Machine(CVM)",
                        "ProductName": "云服务器CVM",
                        "SubBillingItemCode": "",
                        "SubProductCode": "sp_cvm_s2",
                        "SubProductEnName": "CVM Standard S2",
                        "SubProductName": "云服务器CVM-标准型S2"
                    }
                ],
                "UsedAmount": 1000000,
                "UsedTime": "2024-02-12 15:54:56",
                "VoucherId": "WFRCNWBQBHNYJTZ3XLGE3T"
            },
            {
                "PayMode": "postpay",
                "PayScene": null,
                "SeqId": "20240212799000283860282006",
                "UsageDetails": [
                    {
                        "Action": "",
                        "BillingItemCode": "",
                        "CalcUnit": "1",
                        "ProductCode": "p_ccn",
                        "ProductEnName": "Cloud Connect Network",
                        "ProductName": "云联网CCN",
                        "SubBillingItemCode": "",
                        "SubProductCode": "sp_ccn_connecting_instance",
                        "SubProductEnName": "Cloud Connect Network-connecting-instance",
                        "SubProductName": "云联网网络连接实例费"
                    }
                ],
                "UsedAmount": 1000000,
                "UsedTime": "2024-02-12 15:53:33",
                "VoucherId": "WFRCNWBQBHNYJTZ3XLGE3T"
            },
            {
                "PayMode": "postpay",
                "PayScene": null,
                "SeqId": "20240212799000283860282005",
                "UsageDetails": [
                    {
                        "Action": "",
                        "BillingItemCode": "",
                        "CalcUnit": "1",
                        "ProductCode": "p_ccn",
                        "ProductEnName": "Cloud Connect Network",
                        "ProductName": "云联网CCN",
                        "SubBillingItemCode": "",
                        "SubProductCode": "sp_ccn_connecting_instance",
                        "SubProductEnName": "Cloud Connect Network-connecting-instance",
                        "SubProductName": "云联网网络连接实例费"
                    }
                ],
                "UsedAmount": 1000000,
                "UsedTime": "2024-02-12 15:36:54",
                "VoucherId": "WFRCNWBQBHNYJTZ3XLGE3T"
            },
            {
                "PayMode": "prepay",
                "PayScene": "",
                "SeqId": "20240212840001259973831111",
                "UsageDetails": [
                    {
                        "Action": "purchase",
                        "BillingItemCode": "",
                        "CalcUnit": "",
                        "ProductCode": "p_cvm",
                        "ProductEnName": "Cloud Virtual Machine(CVM)",
                        "ProductName": "云服务器CVM",
                        "SubBillingItemCode": "",
                        "SubProductCode": "sp_cvm_s2",
                        "SubProductEnName": "CVM Standard S2",
                        "SubProductName": "云服务器CVM-标准型S2"
                    }
                ],
                "UsedAmount": 1000000,
                "UsedTime": "2024-02-12 15:15:49",
                "VoucherId": "WFRCNWBQBHNYJTZ3XLGE3T"
            },
            {
                "PayMode": "prepay",
                "PayScene": "",
                "SeqId": "20240212840001259973831109",
                "UsageDetails": [
                    {
                        "Action": "purchase",
                        "BillingItemCode": "",
                        "CalcUnit": "",
                        "ProductCode": "p_cvm",
                        "ProductEnName": "Cloud Virtual Machine(CVM)",
                        "ProductName": "云服务器CVM",
                        "SubBillingItemCode": "",
                        "SubProductCode": "sp_cvm_s2",
                        "SubProductEnName": "CVM Standard S2",
                        "SubProductName": "云服务器CVM-标准型S2"
                    }
                ],
                "UsedAmount": 1000000,
                "UsedTime": "2024-02-12 15:14:18",
                "VoucherId": "WFRCNWBQBHNYJTZ3XLGE3T"
            }
        ]
    }
}
```

