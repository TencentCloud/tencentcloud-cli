**Example 1: 示例1**

demo

Input: 

```
tccli wedata DescribeGlobalWorkflowDs --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --Keyword workfl \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "CurrentPage": 1,
            "CurrentPageItems": 10,
            "Items": [
                {
                    "FolderId": "7635d511-b0ea-11ed-8909-bc97e105ba60",
                    "Links": null,
                    "Owner": "harugeng",
                    "OwnerId": "100029682766",
                    "Params": null,
                    "ProjectId": "1491185733977370624",
                    "ProjectIdent": "unified_scheduler",
                    "ProjectName": "Wedata调度三网融合_dev",
                    "SparkParams": "",
                    "Tasks": null,
                    "WorkflowDesc": "1",
                    "WorkflowId": "7db8017c-b0ea-11ed-8909-bc97e105ba60",
                    "WorkflowName": "1"
                },
                {
                    "FolderId": "50a3f793-b11b-11ed-8909-bc97e105ba60",
                    "Links": null,
                    "Owner": "jayshi",
                    "OwnerId": "100028578933",
                    "Params": null,
                    "ProjectId": "1460947878944567296",
                    "ProjectIdent": "us_dev",
                    "ProjectName": "调度dev验证项目",
                    "SparkParams": "",
                    "Tasks": null,
                    "WorkflowDesc": "",
                    "WorkflowId": "5d0bffaf-b11b-11ed-8909-bc97e105ba60",
                    "WorkflowName": "20230220_patch"
                },
                {
                    "FolderId": "50a3f793-b11b-11ed-8909-bc97e105ba60",
                    "Links": null,
                    "Owner": "jayshi",
                    "OwnerId": "100028578933",
                    "Params": null,
                    "ProjectId": "1460947878944567296",
                    "ProjectIdent": "us_dev",
                    "ProjectName": "调度dev验证项目",
                    "SparkParams": "",
                    "Tasks": null,
                    "WorkflowDesc": "",
                    "WorkflowId": "9d9d0c78-b1bb-11ed-8909-bc97e105ba60",
                    "WorkflowName": "20230221_patch"
                },
                {
                    "FolderId": "05561fa3-eb36-11ed-8909-bc97e105ba60",
                    "Links": null,
                    "Owner": "wineliu",
                    "OwnerId": "100029386024",
                    "Params": null,
                    "ProjectId": "1470547050521227264",
                    "ProjectIdent": "wedata_dev_new",
                    "ProjectName": "wedata数据开发_新",
                    "SparkParams": "",
                    "Tasks": null,
                    "WorkflowDesc": "",
                    "WorkflowId": "26464ddf-eb36-11ed-8909-bc97e105ba60",
                    "WorkflowName": "aaa"
                },
                {
                    "FolderId": "17553b8a-adf7-11ed-8909-bc97e105ba60",
                    "Links": null,
                    "Owner": "wineliu",
                    "OwnerId": "100029386024",
                    "Params": null,
                    "ProjectId": "1460947878944567296",
                    "ProjectIdent": "us_dev",
                    "ProjectName": "调度dev验证项目",
                    "SparkParams": "",
                    "Tasks": null,
                    "WorkflowDesc": "",
                    "WorkflowId": "2683a086-adf7-11ed-8909-bc97e105ba60",
                    "WorkflowName": "aaaa"
                },
                {
                    "FolderId": "bc23782a-b1b8-11ed-8909-bc97e105ba60",
                    "Links": null,
                    "Owner": "wineliu",
                    "OwnerId": "100029386024",
                    "Params": null,
                    "ProjectId": "1460947878944567296",
                    "ProjectIdent": "us_dev",
                    "ProjectName": "调度dev验证项目",
                    "SparkParams": "spark.driver.cores=1;\nspark.driver.memory=1g;\nspark.executor.memory=1g;\nspark.executor.instances=1;\nspark.executor.cores=1;\n",
                    "Tasks": null,
                    "WorkflowDesc": "测试",
                    "WorkflowId": "c55762aa-b1b8-11ed-8909-bc97e105ba60",
                    "WorkflowName": "aaaaa"
                },
                {
                    "FolderId": "4ca3fc89-c705-11ed-8909-bc97e105ba60",
                    "Links": null,
                    "Owner": "zenofu",
                    "OwnerId": "100028579464",
                    "Params": null,
                    "ProjectId": "1460947878944567296",
                    "ProjectIdent": "us_dev",
                    "ProjectName": "调度dev验证项目",
                    "SparkParams": "",
                    "Tasks": null,
                    "WorkflowDesc": "",
                    "WorkflowId": "724a2e53-c714-11ed-8909-bc97e105ba60",
                    "WorkflowName": "aaa_w_01"
                },
                {
                    "FolderId": "66f76dee-c714-11ed-8909-bc97e105ba60",
                    "Links": null,
                    "Owner": "zenofu",
                    "OwnerId": "100028579464",
                    "Params": null,
                    "ProjectId": "1460947878944567296",
                    "ProjectIdent": "us_dev",
                    "ProjectName": "调度dev验证项目",
                    "SparkParams": "spark.driver.cores=1;\nspark.driver.memory=1g;\nspark.executor.memory=1g;\nspark.executor.instances=1;\nspark.executor.cores=1;\n",
                    "Tasks": null,
                    "WorkflowDesc": "",
                    "WorkflowId": "7bda1696-c714-11ed-8909-bc97e105ba60",
                    "WorkflowName": "aaa_w_02"
                },
                {
                    "FolderId": "ca01bd07-c7db-11ed-8909-bc97e105ba60",
                    "Links": null,
                    "Owner": "zhanglin",
                    "OwnerId": "100028579801",
                    "Params": null,
                    "ProjectId": "1464962169590902784",
                    "ProjectIdent": "wedata_dev",
                    "ProjectName": "wedata数据开发",
                    "SparkParams": "",
                    "Tasks": null,
                    "WorkflowDesc": "",
                    "WorkflowId": "9e436591-e36c-11ed-8909-bc97e105ba60",
                    "WorkflowName": "aa_wf_230425_01"
                },
                {
                    "FolderId": "34402934-b28a-11ed-8909-bc97e105ba60",
                    "Links": null,
                    "Owner": "abelteng",
                    "OwnerId": "100028663852",
                    "Params": null,
                    "ProjectId": "1460947878944567296",
                    "ProjectIdent": "us_dev",
                    "ProjectName": "调度dev验证项目",
                    "SparkParams": "",
                    "Tasks": null,
                    "WorkflowDesc": "",
                    "WorkflowId": "3a69140a-b28a-11ed-8909-bc97e105ba60",
                    "WorkflowName": "abel"
                }
            ],
            "PageSize": 10,
            "TotalItems": 80,
            "TotalPages": 8
        },
        "RequestId": "1167dc9f-fd39-482c-9a17-45e1b24abaaa"
    }
}
```

