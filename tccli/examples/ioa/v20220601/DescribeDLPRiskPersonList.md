**Example 1: 查询风险员工列表**

查询风险员工列表

Input: 

```
tccli ioa DescribeDLPRiskPersonList --cli-unfold-argument  \
    --Condition.PageSize 10 \
    --Condition.PageNum 0 \
    --BeginTime 1600730187 \
    --EndTime 1700730187
```

Output: 
```
{
    "Response": {
        "RequestId": "dc7b5cee-7d72-4769-b00c-7e38b1ae0220"
    }
}
```

