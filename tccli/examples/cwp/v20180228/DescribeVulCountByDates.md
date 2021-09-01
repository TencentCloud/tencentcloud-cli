**Example 1: 批量获取近日指定类型的漏洞数量和主机数量**

漏洞分类统计-批量获取近日指定类型的漏洞数量和主机数量

Input: 

```
tccli cwp DescribeVulCountByDates --cli-unfold-argument  \
    --LastDays 1 \
    --VulCategory 1
```

Output: 
```
{
    "Response": {
        "HostCount": [
            0,
            0,
            3
        ],
        "RequestId": "req-566234234",
        "VulCount": [
            0,
            0,
            1
        ]
    }
}
```

