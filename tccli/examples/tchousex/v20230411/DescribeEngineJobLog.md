**Example 1: 测试示例**

测试示例

Input: 

```
tccli tchousex DescribeEngineJobLog --cli-unfold-argument  \
    --InstanceId warehouse-qiwlg758 \
    --EngineJobId batch-task-324ztz \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Limit": 0,
        "Logs": null,
        "Offset": 0,
        "RequestId": "93f728dc-8958-4658-b475-0dfe39f9825e"
    }
}
```

