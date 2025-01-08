**Example 1: DescribeStarRocksQueryInfo**



Input: 

```
tccli emr DescribeStarRocksQueryInfo --cli-unfold-argument  \
    --InstanceId emr-1qop4l3e \
    --PageSize 10 \
    --Page 1 \
    --StartTime 1722327682 \
    --EndTime 1722328091
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "StarRocksQueryInfoList": [
            {
                "ClientIP": "192.0.0.1",
                "CPUCost": 0,
                "DefaultDB": "db_test",
                "EndTime": 1721962352,
                "ExecutionIP": "192.0.0.1",
                "QueryID": "1ac25f6c-4afa-11ef-b7cc-525400c756d2",
                "QueryType": "OTHERS",
                "MemCost": 324,
                "PlanCpuCosts": 435620,
                "PlanMemCosts": 254354,
                "QueryTime": 345535,
                "ResourceGroup": "SR",
                "ReturnRows": 2452,
                "ScanBytes": 1235124,
                "ScanRows": 123512,
                "BeginTime": 1721962352,
                "ExecutionState": "FINISHED",
                "ExecutionStatement": "show compute nodes",
                "User": "test_aa"
            }
        ],
        "RequestId": "1ac25f6c-4afa-11ef-b7cc-525400454wfaa1"
    }
}
```

