**Example 1: 查询生产者列表**

查询生产者列表

Input: 

```
tccli trocket DescribeProducerList --cli-unfold-argument  \
    --InstanceId rmq-9j77qmrm \
    --Topic topic-normal \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "ProducerList": [
            {
                "ClientId": "169.254.165.243@a3c02f03-5b27-425f-8632-83d1e9f7010b",
                "ClientIp": "/11.176.16.134:58560",
                "Language": "JAVA",
                "LastUpdateTimestamp": 1725440379597,
                "Version": "V4_9_3"
            }
        ],
        "RequestId": "6918ecdb-ee41-4f8a-bf5f-7b313cd5fca0",
        "TotalCount": 1
    }
}
```

