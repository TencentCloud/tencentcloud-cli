**Example 1: DescribeKyuubiQueryInfo**



Input: 

```
tccli emr DescribeKyuubiQueryInfo --cli-unfold-argument  \
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
        "KyuubiQueryInfoList": [
            {
                "ClientIP": "10.0.2.42",
                "Duration": 5895,
                "EndTime": 1722328097,
                "EngineID": "null",
                "EngineType": "SPARK_SQL",
                "Id": "d4cfc064-b7d9-43ec-a766-60013c592dd4",
                "SessionID": "1c3cdb57-e0b3-489a-804e-662600a24f1d",
                "BeginTime": 1722328091,
                "ExecutionState": "FINISHED",
                "ExecutionStatement": "select * from kyuubi_test.kyuubi_new_user_tb order by id ASC",
                "StatementID": "d4cfc064-b7d9-43ec-a766-60013c592dd4",
                "User": "new_kyuubi_user"
            }
        ],
        "RequestId": "cfbbbe0f-5d30-4bf7-b87b-428b14ac3ws41",
        "TotalCount": 10
    }
}
```

