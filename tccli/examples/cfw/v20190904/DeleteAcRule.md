**Example 1: 删除规则**



Input: 

```
tccli cfw DeleteAcRule --cli-unfold-argument  \
    --Placement.Zone ap-guangzhou-2\
    --ImageId test\
    --Id 1\
    --Direction 1
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

