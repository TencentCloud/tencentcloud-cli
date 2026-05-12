**Example 1: 修改Dspm访问管理信息**



Input: 

```
tccli csip ModifyDspmAccessRecord --cli-unfold-argument  \
    --Id.0.SourceIp 10.10.0.1 \
    --Id.0.AssetId cdb-c2thbt00 \
    --Id.0.RecordTime 2025-03-01 12:00:00 \
    --View ip \
    --Noted 1
```

Output: 
```
{
    "Response": {
        "RequestId": "cf839eee-b651-4ff3-9b49-173f9f55733f"
    }
}
```

