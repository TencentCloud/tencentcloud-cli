**Example 1: 获取慢查询记录**



Input: 

```
tccli sqlserver DescribeSlowlogs --cli-unfold-argument  \
    --InstanceId mssql-njj2mtpl\
    --StartTime '2018-03-28 00:00:00'\
    --EndTime '2018-04-20 00:00:00'\
    --Limit 20\
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "46f65a4e-dd80-4379-a91b-1fb8464e3abf",
        "TotalCount": 0,
        "Slowlogs": []
    }
}
```

