**Example 1: 获取合规系统版本信息**



Input: 

```
tccli sag DescribeComplianceOs --cli-unfold-argument  \
    --Os Windows
```

Output: 
```
{
    "Response": {
        "Data": {
            "OsName": "Windwos 7",
            "OsVersion": "6.1.7600"
        },
        "RequestId": "xx"
    }
}
```

