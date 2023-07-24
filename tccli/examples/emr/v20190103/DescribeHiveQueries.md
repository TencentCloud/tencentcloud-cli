**Example 1: 获取Hive查询语句**

获取Hive查询语句

Input: 

```
tccli emr DescribeHiveQueries --cli-unfold-argument  \
    --InstanceId emr-qy2p6mem \
    --Offset 0 \
    --Limit 2 \
    --StartTime 1685633400 \
    --EndTime 1686239999
```

Output: 
```
{
    "Response": {
        "Total": 287,
        "RequestId": "12345678999",
        "Results": [
            {
                "ExecutionEngine": "mr",
                "Statement": "insert into oozie_hive2 values(1, 'oozie1'),(2, 'oozie2')",
                "JobIds": [
                    "application_1686021938406_0191"
                ],
                "State": "FINISHED",
                "User": "hadoop",
                "StartTime": 1686064102000,
                "Duration": "104ms",
                "EndTime": 1686064207000,
                "Id": "hadoop_20230606150822_d1c216ea-7602-4fc6-9a20-5c0287f062ff"
            },
            {
                "ExecutionEngine": "mr",
                "Statement": "create table if not exists oozie_hive2(id int, name string)",
                "JobIds": [],
                "State": "FINISHED",
                "User": "hadoop",
                "StartTime": 1686064093000,
                "Duration": "8ms",
                "EndTime": 1686064102000,
                "Id": "hadoop_20230606150813_20c9784a-564c-4b80-9505-e46392cbb152"
            }
        ]
    }
}
```

