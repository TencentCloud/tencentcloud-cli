**Example 1: 查询 DB Custom 任务状态**



Input: 

```
tccli dbdc DescribeDBCustomTaskStatus --cli-unfold-argument  \
    --TaskId 74
```

Output: 
```
{
    "Response": {
        "Status": "Succeeded",
        "RequestId": "0d41f891-8589-45c3-8867-311a9df44c05"
    }
}
```

**Example 2: 查询 DB Custom 节点重启任务状态**



Input: 

```
tccli dbdc DescribeDBCustomTaskStatus --cli-unfold-argument  \
    --TaskId 490
```

Output: 
```
{
    "Response": {
        "ResourceStatusSet": [
            {
                "ResourceId": "dbcn-tnjzxz3n",
                "Status": "Succeeded"
            }
        ],
        "Status": "Succeeded",
        "RequestId": "9cbb9215-6b2c-4e84-a9bd-a1afdd299b41"
    }
}
```

