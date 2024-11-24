**Example 1: 示例**



Input: 

```
tccli cdwch ScaleCNOutUpInstance --cli-unfold-argument  \
    --InstanceId clickhouse-cn-xxxxxx \
    --VirtualCluster warehouse3 \
    --UserSubnetID subnet-xxxxxxx \
    --NewCount 2 \
    --NewSpecName 2X-Small
```

Output: 
```
{
    "Response": {
        "InstanceId": "clickhouse-cn-xxxxxx",
        "FlowId": "",
        "RequestId": "01111",
        "ErrorMsg": "addddd"
    }
}
```

