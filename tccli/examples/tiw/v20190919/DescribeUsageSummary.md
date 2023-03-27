**Example 1: 查询子产品用量统计**

查询子产品用量统计

Input: 

```
tccli tiw DescribeUsageSummary --cli-unfold-argument  \
    --BeginTime '2019-12-30 11:41:58' \
    --EndTime '2019-12-30 11:42:06' \
    --SubProducts sp_tiw_dt sp_tiw_st \
    --IsWeighted true
```

Output: 
```
{
    "Response": {
        "RequestId": "70443084-c60f-4f8e-a4f9-acb791802298"
    }
}
```

