**Example 1: 示例**



Input: 

```
tccli rum DescribeIssueTrend --cli-unfold-argument  \
    --AppId 14669 \
    --IssueId 0f5f040e0c3d999eb9557bdb3adcd18253d64785594e80785d443d222de1f \
    --StartTime 1782717720000 \
    --EndTime 1782976920000 \
    --Bucket 11
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "{\"Code\":\"InvalidParameter\",\"Message\":\"bucket 参数无效\"}",
        "RequestId": "8c427f4d-c5da-41bb-8592-df2a60d75428"
    }
}
```

