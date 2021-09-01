**Example 1: 修改单个防火墙开关**



Input: 

```
tccli cfw ModifyItemSwitchStatus --cli-unfold-argument  \
    --Id 341 \
    --Status 1 \
    --Type 1
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

