**Example 1: 批量修改 DNS 记录状态**

在 ZoneId 为 zone-25ryyvog1qih 的站点下，修改记录ID 为 record-25ryzh92h8qh 和 record-dldu75sgz4r1 的 DNS 记录状态为启用，修改记录ID 为 record-gkd9gyrvk8d7 和 record-lgubhs6rf9s3 的 DNS 记录状态为停用。

Input: 

```
tccli teo ModifyDnsRecordsStatus --cli-unfold-argument  \
    --RecordsToEnable record-25ryzh92h8qh record-dldu75sgz4r1 \
    --RecordsToDisable record-gkd9gyrvk8d7 record-lgubhs6rf9s3 \
    --ZoneId zone-25ryyvog1qih
```

Output: 
```
{
    "Response": {
        "RequestId": "952c708d-abaf-464c-84cf-d1447887cf65"
    }
}
```

