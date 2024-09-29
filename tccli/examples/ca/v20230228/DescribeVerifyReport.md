**Example 1: DescribeVerifyReport**

验签报告查询

Input: 

```
tccli ca DescribeVerifyReport --cli-unfold-argument  \
    --SignatureId 6921757****1854336
```

Output: 
```
{
    "Response": {
        "ReportUrl": "https://file.nmgsca.com/verified/*********",
        "RequestId": "292ea5cb-4e80-417c-92fd-02d869545682"
    }
}
```

