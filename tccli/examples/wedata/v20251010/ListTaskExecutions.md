**Example 1: 查询任务运行列表示例**



Input: 

```
tccli wedata ListTaskExecutions --cli-unfold-argument  \
    --WorkspaceId 1 \
    --TaskId t_exec_1001_1 \
    --WorkflowExecutionId exec_1001 \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 0,
            "TotalPageNumber": 0
        },
        "RequestId": "f317ade1-b842-411f-803a-613af482f366"
    }
}
```

