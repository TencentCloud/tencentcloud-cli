**Example 1: 查询任务详情**

查询任务详情。

Input: 

```
tccli omics GetRunStatus --cli-unfold-argument  \
    --RunUuid 84232c68-a016-4668-b2e3-168a175d6f29 \
    --ProjectId prj-peaceful-pink-bird-631828
```

Output: 
```
{
    "Response": {
        "Metadata": {
            "CallCached": false,
            "CallName": "main_workflow",
            "Command": "",
            "EndTime": "2022-10-31T14:11:23+08:00",
            "ErrorMessage": "{}",
            "Input": "{\"main_workflow.base64_in\": \"cos://gene-1252949230/samples.csv\"}",
            "JobId": "",
            "Output": "{\"main_workflow.main_output\": \"cos://gene-1252949230/outputs/import/out/base64/samples.csv.base64\"}",
            "ParentId": "84232c68-a016-4668-b2e3-168a175d6f29",
            "PostProcess": false,
            "Preprocess": true,
            "RunId": "84232c68-a016-4668-b2e3-168a175d6f29",
            "RunType": "Workflow",
            "Runtime": "{}",
            "ScatterIndex": "",
            "StartTime": "2022-10-31T14:10:13+08:00",
            "Status": "SUCCESS",
            "Stderr": "",
            "Stdout": "",
            "SubmitTime": "2022-10-31T14:10:12+08:00"
        },
        "RequestId": "b970585c-c5bb-48e2-ac90-82c59dcadd48"
    }
}
```

