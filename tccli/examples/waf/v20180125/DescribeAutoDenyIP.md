**Example 1: 描述WAF自动封禁IP 详情**



Input: 

```
tccli waf DescribeAutoDenyIP --cli-unfold-argument  \
    --Count 0 \
    --Category  \
    --Domain  \
    --Name  \
    --Ip  \
    --VtsMax 1 \
    --VtsMin 1 \
    --Sort  \
    --Limit 1 \
    --CtsMin 1 \
    --Skip 1 \
    --CtsMax 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Res": [],
            "TotalCount": 0
        },
        "RequestId": "a4010dd1-d24b-43f5-bab4-8a6b204835b7"
    }
}
```

