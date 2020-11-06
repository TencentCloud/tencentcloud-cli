**Example 1: 查询工作流最近一次执行状态**

查询工作流最近一次执行状态

Input: 

```
tccli tsf DescribeFlowLastBatchState --cli-unfold-argument  \
    --FlowId flow-qov7j8ky \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "6281ddf9-1914-420b-afb8-93735ac3270a",
        "Result": {
            "FlowBatchId": "fbatch-2niomsd",
            "State": "SUCCESS"
        }
    }
}
```

