**Example 1: 修改运维任务示例**



Input: 

```
tccli bh ModifyOperationTask --cli-unfold-argument  \
    --Id 10 \
    --Name 运维任务 \
    --Type 1 \
    --Account ubuntu \
    --Timeout 10 \
    --Script ls \
    --Encoding 1 \
    --DeviceIdSet 34 56 47
```

Output: 
```
{
    "Response": {
        "RequestId": "31js-hapqhxmaj-h12knsk2weq"
    }
}
```

