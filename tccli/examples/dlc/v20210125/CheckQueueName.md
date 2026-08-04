**Example 1: check queue name**



Input: 

```
tccli dlc CheckQueueName --cli-unfold-argument  \
    --QueueName default \
    --PartitionCode dlc-p-ofvhyjzn
```

Output: 
```
{
    "Response": {
        "IsValid": "false",
        "Message": "同一分区下队列名称已存在，请使用其他名称",
        "RequestId": "2233e6a9-2829-47fa-ab07-d2b53b80050a"
    }
}
```

