**Example 1: 查询通知模板示例**

查询通知模板示例

Input: 

```
tccli dbbrain DescribeAlarmTemplate --cli-unfold-argument  \
    --TemplateNameRegexp test \
    --Limit 50 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ProfileList": [],
        "RequestId": "5c2ad5eb-784b-4ff4-8860-17f75f4e5c1f",
        "TotalCount": 0
    }
}
```

