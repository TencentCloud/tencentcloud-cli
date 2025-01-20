**Example 1: license统计**

统计各个类型的license数量

Input: 

```
tccli trro GetLicenseStat --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Valid": 10,
        "Bound": 8,
        "UnBound": 2,
        "Expire": 1,
        "MonthlyExpire": 0,
        "RequestId": "72e27b83-97e4-4325-f4e3-cac52c5ed9e3"
    }
}
```

