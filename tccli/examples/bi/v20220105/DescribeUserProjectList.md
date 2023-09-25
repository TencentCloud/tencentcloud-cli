**Example 1: 项目内用户接口示例**



Input: 

```
tccli bi DescribeUserProjectList --cli-unfold-argument  \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "1e7794a2-4f1b-4524-af91-71ed16d0bf8f",
        "Extra": "",
        "Data": {
            "List": [
                {
                    "UserId": "joeyzang",
                    "UserName": "臧洋洲"
                },
                {
                    "UserId": "joshshzhou",
                    "UserName": "周树豪"
                },
                {
                    "UserId": "kiraxie",
                    "UserName": "谢严坤"
                },
                {
                    "UserId": "vanvanchen",
                    "UserName": "陈凡凡"
                },
                {
                    "UserId": "abbiezhan",
                    "UserName": "詹薇"
                },
                {
                    "UserId": "allenxfwang",
                    "UserName": "王先飞"
                },
                {
                    "UserId": "bluelishen",
                    "UserName": "沈立"
                },
                {
                    "UserId": "600000560068",
                    "UserName": "沈立"
                }
            ],
            "Total": 8,
            "TotalPages": 0
        },
        "Msg": "success"
    }
}
```

