**Example 1: 示例**



Input: 

```
tccli rum DescribeIssueEvents --cli-unfold-argument  \
    --AppId 146692 \
    --IssueId ca5ac1fb1f4d2993581ea232a73d4575e69579f254f110460c544117ae275fd9 \
    --StartTime 1781420460000 \
    --EndTime 1781689660000 \
    --Keyword 这是 \
    --Filters [{"Key":"app_version","Op":"eq","Values":"2.0.4"}] \
    --Page 1 \
    --PageSize 20
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "{\"Code\":\"InvalidParameter\",\"Message\":\"Filters JSON 解析失败: json: cannot unmarshal string into Go struct field CAPIFilter.Values of type []string\"}",
        "RequestId": "af852781-2f64-4cde-bb80-919c5df34531"
    }
}
```

