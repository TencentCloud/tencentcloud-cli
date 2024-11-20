**Example 1: DescribeBillDetail**

子客查询l3账单
	
POST / HTTP/1.1

Host: intlpartnersmgt.tencentcloudapi.com
Content-Type: application/json
X-TC-Action: DescribeCustomerBillDetail
<公共请求参数>



Input: 

```
tccli intlpartnersmgt DescribeBillDetail --cli-unfold-argument  \
    --Month 2023-02 \
    --PayMode postPay \
    --ActionType postpay_deduct_h \
    --PageSize 10 \
    --Page 1
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "DetailSet": [
            {
                "PayerAccountId": 1230,
                "OwnerAccountId": 132,
                "OperatorAccountId": 321,
                "ProductName": "cloud block storage",
                "BillingMode": "Pay-As-You-Go resources",
                "ProjectName": "default",
                "Region": "East Chinaxa0(Shanghai)",
                "AvailabilityZone": "Shanghai Zone 1",
                "InstanceId": "disk-4jrmzpvk",
                "InstanceName": "the name",
                "SubProductName": "HDD cloud block storage",
                "TransactionType": "Hourly settlement",
                "TransactionId": "2023010112345678",
                "TransactionTime": "2023-01-01 00:01:02",
                "UsageStartTime": "2023-01-01 00:01:02",
                "UsageEndTime": "2023-01-01 00:01:02",
                "ComponentType": "volume size",
                "ComponentName": "HDD cloud block storage-volume size",
                "ComponentListPrice": "0.1",
                "ComponentPriceMeasurementUnit": "USD/GB/Second",
                "ComponentUsage": "100",
                "ComponentUsageUnit": "GB",
                "UsageDuration": "100",
                "DurationUnit": "Second",
                "OriginalCost": "10",
                "Currency": "USD",
                "TotalCost": "10"
            }
        ],
        "RequestId": "asdfgh"
    }
}
```

