**Example 1: 异步导入激活码包**



Input: 

```
tccli trp CreateTraceCodesAsync --cli-unfold-argument  \
    --BatchId 20241022112952826 \
    --FileKey anxin/filekeyname.zip
```

Output: 
```
{
    "Response": {
        "BatchId": "20241022112952826",
        "RequestId": "384f8d0c-0c15-4dce-9b23-85ca839364ad"
    }
}
```

