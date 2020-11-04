**Example 1: 防火墙状态列表**



Input: 

```
tccli cfw DescribeSwitchLists --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2\
    --ImageId test
```

Output: 
```
{
    "Response": {
        "Total": 110,
        "Data": [],
        "AreaLists": [],
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

