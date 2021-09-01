**Example 1: 防火墙开关列表**



Input: 

```
tccli cfw DescribeSwitchLists --cli-unfold-argument  \
    --SearchValue  \
    --Status -1 \
    --Type  \
    --Area  \
    --Limit 10 \
    --Offset 0 \
    --Order  \
    --By 
```

Output: 
```
{
    "Response": {
        "Total": 110,
        "Data": [],
        "AreaLists": [],
        "OffNum": 10,
        "OnNum": 10,
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

