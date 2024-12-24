**Example 1: 删除 DNS 记录**

在 ZoneId 为 zone-25ryyvog1qih 的站点下，删除记录 ID 为 record-25ryzh92h8qh 和 record-3suf7slrsobg 的 DNS 记录。

Input: 

```
tccli teo DeleteDnsRecords --cli-unfold-argument  \
    --RecordIds record-25ryzh92h8qh record-3suf7slrsobg \
    --ZoneId zone-25ryyvog1qih
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

