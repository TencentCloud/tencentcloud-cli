**Example 1: 示例 1**



Input: 

```
tccli billing DescribeRenewInstances --cli-unfold-argument  \
    --MaxResults 10 \
    --NextToken VDAwMSu3Y69lZhLwW1bRxLiwKafWBv_6TqKBnp-YH12b0uWcwTBf3DIK7Myza6EVdhDKoFGpKANnZkfmmLy5K8uH1lJYqyvuT_mSXc8VoOdX-8kcKJrB3JbyW9dM0edrKm3Q \
    --Reverse True \
    --RenewFlagList DISABLE_NOTIFY_AND_MANUAL_RENEW \
    --InstanceIdList std_storage-20241106185002290002691-0 \
    --ExpireTimeStart 2025-06-26 00:38:46 \
    --ExpireTimeEnd 2025-09-27 15:38:46
```

Output: 
```
{
    "Response": {
        "InstanceList": [
            {
                "ExpireTime": "2025-07-06 23:59:59",
                "InstanceId": "std_storage-20241106185002290002691-0",
                "InstanceName": "",
                "ProductCode": "p_cos",
                "ProductName": "COS u5bf9u8c61u5b58u50a8",
                "ProjectName": "u9ed8u8ba4u9879u76ee",
                "RegionCode": "ap-others",
                "RenewFlag": "DISABLE_NOTIFY_AND_MANUAL_RENEW",
                "RenewPeriod": 1,
                "RenewPeriodUnit": "m",
                "Status": "NORMAL",
                "SubProductCode": "sp_cos_pkg_std_new"
            }
        ],
        "NextToken": null,
        "RequestId": "6e1a3451-b75c-4d7d-bbbd-e363682ab0af"
    }
}
```

