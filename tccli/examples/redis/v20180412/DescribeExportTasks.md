**Example 1: 请求实例**



Input: 

```
tccli redis DescribeExportTasks --cli-unfold-argument  \
    --LogType auditLog \
    --Limit 10 \
    --Offset 0 \
    --InstanceId crs-f9o8****
```

Output: 
```
{
    "Response": {
        "Items": [],
        "TotalCount": 0,
        "RequestId": "4f66033b-2ea9-406c-9228-57ddb0b2e01c"
    }
}
```

