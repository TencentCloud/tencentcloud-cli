**Example 1: 编辑状态机**



Input: 

```
tccli asw ModifyFlowService --cli-unfold-argument  \
    --FlowServiceName flowservicetest \
    --FlowServiceResource qrn:qcs:asw:ap-guangzhou:1300000779:http:json:flowmachine:wintest:bg0rx4qy \
    --Definition "{}" \
    --FlowServiceChineseName 工作流中文名称 \
    --IsNewRole false \
    --Type EXPRESS \
    --RoleResource qrn:qcs:asw:ap-guangzhou:1300000779:http:json \
    --EnableCLS true
```

Output: 
```
{
    "Response": {
        "FlowServiceResource": "qrn:qcs:asw:ap-guangzhou:1300000779:http:json:flowmachine:wintest:bg0rx4qy",
        "UpdateDate": "1596628154044",
        "RequestId": "ab1b30fc-3503-4b27-96dc-94c14d2fd43q"
    }
}
```

