**Example 1: 样例**



Input: 

```
tccli wedata DescribeDataSourceList --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "Data": {
            "TotalCount": 10
        }
    }
}
```

