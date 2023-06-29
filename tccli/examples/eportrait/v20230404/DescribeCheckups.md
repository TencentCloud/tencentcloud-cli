**Example 1: DescribeCheckups1**

DescribeCheckups1

Input: 

```
tccli eportrait DescribeCheckups --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Eid e3e41dce9bbd62a5db5a8c9667969103
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Date": "2020-02-21",
                "Department": "广州市海珠区市场监督管理局",
                "Result": "未发现问题",
                "Type": "检查"
            },
            {
                "Date": "2020-08-26",
                "Department": "广州市海珠区市场监督管理局",
                "Result": "未发现问题",
                "Type": "检查"
            },
            {
                "Date": "2020-09-09",
                "Department": "广州市海珠区市场监督管理局",
                "Result": "未发现问题",
                "Type": "检查"
            },
            {
                "Date": null,
                "Department": "广东省统计局",
                "Result": "正常",
                "Type": "抽查"
            }
        ],
        "RequestId": "1b5daccc-7b59-448d-856a-723f3fa259c8",
        "TotalCount": 4
    }
}
```

