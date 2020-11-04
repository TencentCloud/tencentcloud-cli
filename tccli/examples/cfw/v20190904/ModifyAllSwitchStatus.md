**Example 1: 一键开启和关闭**



Input: 

```
tccli cfw ModifyAllSwitchStatus --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2\
    --ImageId test\
    --Status -1
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

