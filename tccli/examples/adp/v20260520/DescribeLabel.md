**Example 1: 查询标签详情**

查询标签详情

Input: 

```
tccli adp DescribeLabel --cli-unfold-argument  \
    --KbId 2021487500370535744 \
    --LabelId 2097607550895843008 \
    --LastTermId 2097607550895843009 \
    --Limit 20 \
    --Query 
```

Output: 
```
{
    "Response": {
        "Summary": {
            "LabelId": "2097607550895843008",
            "Name": "666a",
            "TermTotalCount": 1,
            "TermList": [],
            "RefCount": 0,
            "MetaValue": null
        },
        "RequestId": "9da30b82-26a4-4de4-968e-5cd5cfb80b00"
    }
}
```

