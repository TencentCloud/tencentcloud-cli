**Example 1: 查询简单命名空间列表**



Input: 

```
tccli tsf DescribeSimpleNamespaces --cli-unfold-argument  \
    --Offset 0 \
    --Limit 50
```

Output: 
```
{
    "Response": {
        "RequestId": "44c883b4-9500-43f1-bd42-5bdbfcd5d3f5",
        "Result": {
            "TotalCount": 0,
            "Content": []
        }
    }
}
```

