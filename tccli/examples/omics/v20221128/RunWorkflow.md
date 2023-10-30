**Example 1: 运行工作流**



Input: 

```
tccli omics RunWorkflow --cli-unfold-argument  \
    --ProjectId prj-zealous-black-seagull-241194 \
    --Name taxprofiler \
    --EnvironmentId env-9gapsr23 \
    --GitSource.GitHttpPath https://e.coding.net/omics/test/taxprofiler.git \
    --GitSource.Branch master \
    --Type NEXTFLOW \
    --NFOption.Config  \
    --NFOption.Profile test \
    --InputCosUri cos://bucket-10000/nextflow/taxprofiler/input/input.json
```

Output: 
```
{
    "Response": {
        "RunGroupId": "run-greedy-cerise-swan-618086",
        "RequestId": "5c4fc8c5-d8b1-4041-8198-b4154c0ed15f"
    }
}
```

