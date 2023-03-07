**Example 1: 根据活动链接获取活动信息**

根据活动链接获取活动非敏感信息

Input: 

```
tccli opc DescribeActivityInfoByPageURL --cli-unfold-argument  \
    --PageURL https://cloud.tencent.com/act/pro/jensen-test-0119-1
```

Output: 
```
{
    "Response": {
        "ActivityNonSensitiveInfo": {
            "ActivityId": 12266,
            "EndTime": "2200-08-28 23:59:59",
            "Name": "jensen-test-0119-1",
            "PageUrl": "https://cloud.tencent.com/act/pro/jensen-test-0119-1",
            "StartTime": "2022-01-01 00:00:00",
            "Status": 0
        },
        "RequestId": "21537ecd-2ad8-4b1d-a987-4e977105a4e9"
    }
}
```

