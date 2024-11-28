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
        "TotalUsedAmount": 10000000,
        "TotalCount": 1,
        "RequestId": "1820282306173927424",
        "UsageRecords": [
            {
                "UsedAmount": 10000000,
                "PayScene": "common",
                "UsedTime": "2024-03-29 02:03:27",
                "VoucherId": "VHPIUDFG9GUZDESWPR4W99",
                "SeqId": "10071_2024032902_1300223973_1711649007",
                "UsageDetails": [
                    {
                        "Action": "purchase",
                        "BillingItemCode": "v_cvm_bandwidth",
                        "SubProductName": "云服务器CVM-标准型S1",
                        "SubProductEnName": "CVM Standard S1",
                        "ProductName": "云服务器CVM",
                        "ProductCode": "cvm",
                        "SubBillingItemCode": "sv_cvm_bandwidth_prepay",
                        "ProductEnName": "Cloud Virtual Machine(CVM)",
                        "CalcUnit": "1",
                        "SubProductCode": "p_cvm"
                    }
                ],
                "PayMode": "postpay"
            }
        ]
    }
}
```

