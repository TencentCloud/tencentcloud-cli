**Example 1: 获取指定类型的待处理漏洞数、主机数和非专业版主机数量**

获取指定类型的待处理漏洞数、主机数和非专业版主机数量

Input: 

```
tccli cwp DescribeUndoVulCounts --cli-unfold-argument  \
    --VulCategory 2
```

Output: 
```
{
    "Response": {
        "NotProfessionCount": 1,
        "RequestId": "req-566234234",
        "UndoHostCount": 1,
        "UndoVulCount": 1
    }
}
```

