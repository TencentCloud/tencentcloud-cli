**Example 1: 修改投递COS任务**

修改投递COS任务

Input: 

```
tccli cls ModifyShipper --cli-unfold-argument  \
    --ShipperId xxxx-xx-xx-xx-xxxxxxxx \
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
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

