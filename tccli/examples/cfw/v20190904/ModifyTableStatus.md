**Example 1: 修改规则表状态**



Input: 

```
tccli cfw ModifyTableStatus --cli-unfold-argument  \
    --EdgeId edge-ppt3pi01 \
    --Area ap-guangzhou \
    --Status 2 \
    --Direction 1
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

