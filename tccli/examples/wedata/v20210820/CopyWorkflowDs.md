**Example 1: 示例1**

demo

Input: 

```
tccli wedata CopyWorkflowDs --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --WorkflowId e5b0945c-ed6d-11ed-8909-bc97e105ba60 \
    --WorkflowName workflow_2_copy_1 \
    --WorkflowDesc this is copy workflow \
    --FolderId 37db1991-ed4d-11ed-8909-bc97e105ba60
```

Output: 
```
{
    "Response": {
        "Data": "f5621ee8-ed6d-11ed-8909-bc97e105ba60",
        "RequestId": "82fa7cbb-5b43-4fcf-a220-1a57fcd7b712"
    }
}
```

