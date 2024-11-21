**Example 1: 查询扫码统计记录**

分页查询某批次的扫码统计记录

Input: 

```
tccli trp DescribeScanStats --cli-unfold-argument  \
    --BatchId 20241022112952826 \
    --CorpId 10000 \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "ScanStats": [],
        "RequestId": "RequestId"
    }
}
```

