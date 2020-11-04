**Example 1: 修改单个防火墙开关**



Input: 

```
tccli cfw ModifyItemSwitchStatus --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2\
    --ImageId test\
    --Id 1\
    --Status 1
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

