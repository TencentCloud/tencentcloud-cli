**Example 1: 查询作业详情**

查询作业详情。

Input: 

```
tccli omics GetRunCalls --cli-unfold-argument  \
    --RunUuid 84232c68-a016-4668-b2e3-168a175d6f29 \
    --ProjectId prj-peaceful-pink-bird-631828 \
    --Path /
```

Output: 
```
{
    "Response": {
        "Calls": [
            {
                "CallCached": false,
                "CallName": "sub_workflow",
                "Command": "",
                "EndTime": "2022-10-31T14:11:18+08:00",
                "ErrorMessage": "{}",
                "Input": "{\"base64_in\": \"/cfs-10-8-16-3/omics/file_cache/gene-1252949230/samples.csv\"}",
                "JobId": "",
                "Output": "{\"sub_workflow.sub_output\": \"/cfs-10-8-16-3/cluster/omics-a6z22tn9/execution/main_workflow/84232c68-a016-4668-b2e3-168a175d6f29/call-sub_workflow/sub_workflow/ed4199e3-3513-444e-9090-3413fd6d3e44/call-base64/base64/87ab7713-6f0f-4452-8da9-fbaa40f7e567/call-encode_base64/execution/base64/samples.csv.base64\"}",
                "ParentId": "84232c68-a016-4668-b2e3-168a175d6f29",
                "PostProcess": false,
                "Preprocess": true,
                "RunId": "ed4199e3-3513-444e-9090-3413fd6d3e44",
                "RunType": "Workflow",
                "Runtime": "{}",
                "ScatterIndex": "",
                "StartTime": "2022-10-31T14:10:15+08:00",
                "Status": "COMPLETE",
                "Stderr": "",
                "Stdout": "",
                "SubmitTime": null,
                "Meta": ""
            }
        ],
        "RequestId": "e954d872-2955-4592-901e-38cb6678b88c"
    }
}
```

**Example 2: 查询子作业详情**

查询子作业详情。需要指定Path为上一级GetRunCalls中RunType为Workflow或者Scatter项目的RunId。

Input: 

```
tccli omics GetRunCalls --cli-unfold-argument  \
    --RunUuid 84232c68-a016-4668-b2e3-168a175d6f29 \
    --ProjectId prj-peaceful-pink-bird-631828 \
    --Path /ed4199e3-3513-444e-9090-3413fd6d3e44
```

Output: 
```
{
    "Response": {
        "Calls": [
            {
                "CallCached": false,
                "CallName": "base64",
                "Command": "",
                "EndTime": "2022-10-31T14:11:15+08:00",
                "ErrorMessage": "{}",
                "Input": "{\"input_file\": \"/cfs-10-8-16-3/omics/file_cache/gene-1252949230/samples.csv\"}",
                "JobId": "",
                "Output": "{\"base64.output_file\": \"/cfs-10-8-16-3/cluster/omics-a6z22tn9/execution/main_workflow/84232c68-a016-4668-b2e3-168a175d6f29/call-sub_workflow/sub_workflow/ed4199e3-3513-444e-9090-3413fd6d3e44/call-base64/base64/87ab7713-6f0f-4452-8da9-fbaa40f7e567/call-encode_base64/execution/base64/samples.csv.base64\"}",
                "ParentId": "ed4199e3-3513-444e-9090-3413fd6d3e44",
                "PostProcess": false,
                "Preprocess": true,
                "RunId": "87ab7713-6f0f-4452-8da9-fbaa40f7e567",
                "RunType": "Workflow",
                "Runtime": "{}",
                "ScatterIndex": "",
                "StartTime": "2022-10-31T14:10:17+08:00",
                "Status": "COMPLETE",
                "Stderr": "",
                "Stdout": "",
                "SubmitTime": null,
                "Meta": ""
            }
        ],
        "RequestId": "35431cd8-6913-4c28-808f-290268cb9813"
    }
}
```

