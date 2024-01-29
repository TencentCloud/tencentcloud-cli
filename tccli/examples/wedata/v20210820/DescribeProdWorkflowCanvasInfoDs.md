**Example 1: 示例1**

demo

Input: 

```
tccli wedata DescribeProdWorkflowCanvasInfoDs --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --WorkflowId f5d1b42f-ed67-11ed-8909-bc97e105ba60
```

Output: 
```
{
    "Response": {
        "Data": {
            "FolderId": "37db1991-ed4d-11ed-8909-bc97e105ba60",
            "Links": [],
            "Owner": "jaydenjhu",
            "OwnerId": "100028664112",
            "Params": null,
            "ProjectId": "1460947878944567296",
            "ProjectIdent": "us_dev",
            "ProjectName": "调度dev验证项目",
            "SparkParams": "spark.driver.cores=1;\nspark.driver.memory=1g;\nspark.executor.memory=1g;\nspark.executor.instances=1;\nspark.executor.cores=1;\n",
            "Tasks": [],
            "WorkflowDesc": "",
            "WorkflowId": "f5d1b42f-ed67-11ed-8909-bc97e105ba60",
            "WorkflowName": "workflow_1"
        },
        "RequestId": "86a74dba-965e-41d1-b85b-ccfabbb2be33"
    }
}
```

