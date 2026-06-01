**Example 1: 列脱敏修改**



Input: 

```
tccli tchousex OperateDataMask --cli-unfold-argument  \
    --ApiType Update \
    --PolicyId 285 \
    --InstanceId instance-dgl3qg4g \
    --PolicyName ex_tmcam_simple \
    --User user \
    --Database inside_db \
    --Table ex_tmcam_simple \
    --Columns f12_char f13_char f14_char f15_char \
    --ValueExpr Redact MaskShowFirst4 MaskShowLast4 NULL
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "ReturnData": "null",
        "RequestId": "1ecd9410-9110-4a23-933c-2473759c4ab0"
    }
}
```

