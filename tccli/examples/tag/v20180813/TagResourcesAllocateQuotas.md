**Example 1: 为资源绑定标签预分配配额**

为资源绑定标签预分配配额。

Input: 

```
tccli tag TagResourcesAllocateQuotas --cli-unfold-argument  \
    --ResourceTypeQuotasList.0.ResourceType qcs::redis:ap-beijing::instance/* \
    --ResourceTypeQuotasList.0.Quotas 1 \
    --Tags.0.TagKey k \
    --Tags.0.TagValue v \
    --QuotasExpiredTimestamp 1678335045 \
    --DryRun True
```

Output: 
```
{
    "Response": {
        "RequestId": "9880017c-8d4c-45b1-84f1-36e4xxxxxxc3"
    }
}
```

