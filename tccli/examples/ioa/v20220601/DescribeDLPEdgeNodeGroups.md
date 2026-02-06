**Example 1: 查询分组**



Input: 

```
tccli ioa DescribeDLPEdgeNodeGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "EdgeCount": 0,
                    "GroupId": "d2hhqff7sdjjc675mp9g",
                    "GroupName": "测试_6",
                    "Id": 11
                },
                {
                    "EdgeCount": 0,
                    "GroupId": "d2hhqdv7sdjjc675mp90",
                    "GroupName": "测试_5",
                    "Id": 10
                }
            ],
            "Page": {
                "PageCount": 1,
                "PageNum": 1,
                "PageSize": 10,
                "Total": 9
            }
        },
        "RequestId": "0f420f64-418a-42d1-900d-7620408f0aa6"
    }
}
```

