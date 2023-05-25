**Example 1: 列出已购买预留实例计费**

列出已购买预留实例计费

Input: 

```
tccli cvm DescribeReservedInstances --cli-unfold-argument  \
    --Filters.0.Name zone \
    --Filters.0.Values ap-guangzhou-1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ReservedInstancesSet": [
            {
                "ReservedInstanceId": "ri-rtbh4han",
                "ReservedInstancesId": "ri-rtbh4han",
                "ReservedInstanceName": "riname-01",
                "InstanceType": "S3.16XLARGE256",
                "InstanceFamily": "S3",
                "Zone": "ap-guangzhou-1",
                "StartTime": "0000-00-00 00:00:00",
                "EndTime": "0000-00-00 00:00:00",
                "Duration": 31536000,
                "InstanceCount": 1,
                "ProductDescription": "linux",
                "State": "active",
                "CurrencyCode": "USD",
                "OfferingType": "All Upfront"
            }
        ],
        "RequestId": "9cb3dd3d-5717-47c4-bf3b-05c7ddb4655b"
    }
}
```

