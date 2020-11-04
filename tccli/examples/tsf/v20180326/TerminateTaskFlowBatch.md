**Example 1: 停止一个工作流批次**

停止一个工作流批次

Input: 

```
tccli tsf TerminateTaskFlowBatch --cli-unfold-argument  \
    --FlowBatchId fbatch-6g4rq8z6
```

Output: 
```
{
    "Response": {
        "Result": "false"
    }
}
```

