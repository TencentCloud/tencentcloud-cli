**Example 1: 资产扫描**



Input: 

```
tccli cfw ModifyAssetScan --cli-unfold-argument  \
    --ScanRange 1 \
    --ScanDeep heavy \
    --RangeType 2 \
    --ScanPeriod 每周-星期四/12:51:00 \
    --ScanFilterIp 11 22
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

