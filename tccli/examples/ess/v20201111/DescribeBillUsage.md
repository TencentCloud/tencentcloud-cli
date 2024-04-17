**Example 1: 查询失败样例**



Input: 

```
tccli ess DescribeBillUsage --cli-unfold-argument  \
    --StartTime 20230902 \
    --EndTime 20230930 \
    --QuotaType AAAAA
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.InvalidQuotaType",
            "Message": "非法的套餐类型"
        },
        "RequestId": "s169935778xxxxxxx"
    }
}
```

