**Example 1: 查询在线客服记录示例**



Input: 

```
tccli ccc DescribeIMCdrs --cli-unfold-argument  \
    --InstanceId 12\
    --StartTimestamp 1603877878\
    --EndTimestamp 1603877879
```

Output: 
```
{
    "Response": {
        "IMCdrs": [],
        "TotalCount": 0,
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

