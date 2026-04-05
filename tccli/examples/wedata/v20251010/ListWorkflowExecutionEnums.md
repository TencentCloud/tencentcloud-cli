**Example 1: 查询工作流运行业务枚举**



Input: 

```
tccli wedata ListWorkflowExecutionEnums --cli-unfold-argument  \
    --WorkspaceId 1 \
    --Type 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "BizEnumInfos": [
                {
                    "Count": 1,
                    "LabelKey": "FAILED",
                    "LabelValue": "失败"
                }
            ]
        },
        "RequestId": "5eee3087-a2b2-4038-acf4-8e66c0fa6c86"
    }
}
```

