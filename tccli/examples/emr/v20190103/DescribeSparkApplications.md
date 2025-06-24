**Example 1: 获取spark应用列表**



Input: 

```
tccli emr DescribeSparkApplications --cli-unfold-argument  \
    --InstanceId emr-j14o941k \
    --PageSize 10 \
    --StartTime 1745944098 \
    --EndTime 1746030498 \
    --Page 1
```

Output: 
```
{
    "Response": {
        "RequestId": "RequestId-1746503327",
        "ResultList": [
            {
                "ID": "spark-49cdc7a5b06a46fca99c497a5b47e7f1",
                "Name": "kyuubi_CONNECTION_SPARK_SQL_hadoop_7043f4f2-c8b6-4681-8e7a-873e477c6db7",
                "User": "hadoop",
                "StartTime": 1746003194374,
                "EndTime": 1746003394835,
                "Duration": 200461,
                "State": "completed",
                "ApplicationType": "SPARK",
                "CoreSeconds": 478,
                "MemorySeconds": "489472 MB Seconds",
                "Insight": "UNKNOWN"
            }
        ],
        "TotalCount": 1
    }
}
```

