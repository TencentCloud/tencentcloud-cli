**Example 1: 查询可回档时间范围**



Input: 

```
tccli mariadb DescribeBinlogTime --cli-unfold-argument  \
    --InstanceId tdsql-arryr5nt
```

Output: 
```
{
    "Response": {
        "EndTime": "2019-04-06 14:31:56",
        "RequestId": "8668c08c-e030-48a4-9e67-0c87608f6171",
        "StartTime": "2019-04-06 00:31:10"
    }
}
```

