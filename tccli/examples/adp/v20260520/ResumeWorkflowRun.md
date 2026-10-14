**Example 1: 继续执行等待输入的异步工作流运行实例**

继续执行等待输入的异步工作流运行实例

Input: 

```
tccli adp ResumeWorkflowRun --cli-unfold-argument  \
    --AppId 2075134221221714816 \
    --WorkflowRunId wfr-cd6a2j03k5j4 \
    --Query 买奇瑞汽车
```

Output: 
```
{
    "Response": {
        "RequestId": "956fcc99-f94d-4ad1-87ab-e1f4115577b5"
    }
}
```

