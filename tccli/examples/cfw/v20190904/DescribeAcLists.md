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
        "AllTotal": 1,
        "Total": 1,
        "Data": [
            {
                "Count": 1,
                "Protocol": "xx",
                "Detail": "xx",
                "Strategy": 1,
                "LogId": "xx",
                "OrderIndex": 1,
                "TargetIp": "xx",
                "Port": "xx",
                "SourceIp": "xx",
                "Id": 1
            }
        ],
        "Enable": 1,
        "RequestId": "xx"
    }
}
```

