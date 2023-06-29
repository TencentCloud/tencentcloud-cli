**Example 1: 查询企业经营异常列表**

查询企业经营异常列表

Input: 

```
tccli eportrait DescribeAbnormal --cli-unfold-argument  \
    --Limit 0 \
    --Offset 0 \
    --Eid abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Data": [
            {
                "OutReason": "abc",
                "InDate": "abc",
                "InReason": "abc",
                "Eid": "abc",
                "OutDate": "abc",
                "Department": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

