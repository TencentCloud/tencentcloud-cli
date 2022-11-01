**Example 1: 查询多个服务**



Input: 

```
tccli tione DescribeModelServices --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Services": [
            {
                "UpdateTime": "2021-12-12T21:12:00+08:00",
                "ServiceGroupId": "ms-4jjrcsw2-1",
                "CreatedBy": "yourname",
                "Region": "ap-guangzhou",
                "ServiceGroupName": "test",
                "ServiceId": "ms-4jjrcsw2-1-dfjerxjfe",
                "CreateTime": "2021-12-12T20:12:00+08:00",
                "ServiceDescription": "测试"
            }
        ],
        "TotalCount": 20,
        "RequestId": "fdfahfdjoier"
    }
}
```

