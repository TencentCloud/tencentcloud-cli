**Example 1: 创建投递规则**

用于创建cos投递任务规则

Input: 

```
tccli cls CreateShipper --cli-unfold-argument  \
    --TopicId xxxx-xx-xx-xx-xxxxxxxx \
    --Bucket test-1250000001 \
    --Prefix test \
    --ShipperName myname \
    --Interval 300 \
    --MaxSize 256 \
    --Partition %Y%m%d \
    --Compress.Format none \
    --FilterRules.0.Key  \
    --FilterRules.0.Regex  \
    --FilterRules.0.Value  \
    --FilenameMode 0
```

Output: 
```
{
    "Response": {
        "ShipperId": "xxxx-xx-xx-xx-xxxxxxxx",
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

