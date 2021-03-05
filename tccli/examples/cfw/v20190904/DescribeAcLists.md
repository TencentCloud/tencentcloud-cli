**Example 1: 访问控制列表**



Input: 

```
tccli cfw DescribeAcLists --cli-unfold-argument  \
    --EdgeId  \
    --Protocol TCP \
    --Strategy  \
    --SearchValue  \
    --Direction 1 \
    --Limit 20 \
    --Offset 0 \
    --Area 
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "AllTotal": 0,
        "Enable": 1,
        "Data": []
    }
}
```

