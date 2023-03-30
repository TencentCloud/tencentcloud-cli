**Example 1: 查询集群队列概览信息列表**

查询集群队列概览信息列表。

Input: 

```
tccli thpc DescribeQueues --cli-unfold-argument  \
    --ClusterId hpc-prkxbd7c \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "QueueSet": [
            {
                "QueueName": "compute"
            }
        ],
        "TotalCount": 1,
        "RequestId": "13ee84a5-7846-4682-8877-1c8f94962dd5"
    }
}
```

