**Example 1: 成功示例**

成功示例

Input: 

```
tccli wedata ModifyTaskLinksDs --cli-unfold-argument  \
    --ProjectId 1492511691706699776 \
    --TaskFrom 20240307211633923 \
    --TaskTo 20240307211852581 \
    --LinkDependencyType real_real \
    --WorkflowId ca1253e8-dc84-11ee-8d13-a4ae120f8272 \
    --RealFromWorkflowId ca1253e8-dc84-11ee-8d13-a4ae120f82sda
```

Output: 
```
{
    "Response": {
        "Data": true,
        "LinkId": "ca125988-dc84-11ee-8d13-a4ae120f8272",
        "RequestId": "ca1sad259-dc84-11ee-8d13-a4ae120f8272"
    }
}
```

