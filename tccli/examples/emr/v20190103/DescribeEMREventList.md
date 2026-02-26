**Example 1: 查询EMR事件详情**

通过事件相关信息查询EMR集群的事件详情信息

Input: 

```
tccli emr DescribeEMREventList --cli-unfold-argument  \
    --InstanceId emr-jhpvgwao \
    --StartTime 1767750493 \
    --EndTime 1767756493 \
    --Offset 0 \
    --Limit 2
```

Output: 
```
{
    "Response": {
        "EventList": [
            {
                "CreateTime": "2026-01-07T11:23:32Z",
                "Detail": "HDFS NameNode has not performed Checkpoint for an extended period",
                "Host": "10.0.17.5",
                "Name": "HDFS NameNode长时间未做 Checkpoint",
                "Role": "NameNode"
            },
            {
                "CreateTime": "2026-01-07T11:23:01Z",
                "Detail": "Node:10.0.17.5,  allocated memory >= alarm threshold: 90 \n Memory Node:32768MB \nDeployment component memory Roles HDFS:NN:4096.00MB HIVE:H2:4096.00MB HIVE:HMS:4096.00MB IMPALA:CATALOG:7079.50MB TRINO:M:3072.00MB YARN:AH:3072.00MB YARN:JH:1024.00MB YARN:RM:2000.00MB ZK:QM:1024.00MB  ",
                "Host": "10.0.17.5",
                "Name": "节点内存使用配置超过阈值",
                "Role": "CPU"
            }
        ],
        "RequestId": "7e40cf0a-1208-4fe2-a964-6568d8583cf4",
        "TotalNum": 37
    }
}
```

