**Example 1: 查看禁止扫描目标**

查看禁止扫描目标

Input: 

```
tccli ctem DescribeBannedTargets --cli-unfold-argument  \
    --CustomerId 100136
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppId": 1300055108,
                "CreateAt": "2024-06-07 15:21:07",
                "CustomerId": 100136,
                "CustomerName": "22",
                "From": "",
                "Id": 204,
                "OldId": 0,
                "Remark": "",
                "Target": "a.cn",
                "Uin": "600000560604"
            }
        ],
        "RequestId": "92e36b91-6076-44f2-8323-989b210c640a",
        "Total": 1
    }
}
```

