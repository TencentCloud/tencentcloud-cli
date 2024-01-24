**Example 1: 成功示例**

成功示例

Input: 

```
tccli wedata ModifyTaskLinksDs --cli-unfold-argument  \
    --ProjectId abc \
    --TaskFrom abc \
    --TaskTo abc \
    --LinkDependencyType abc \
    --WorkflowId abc \
    --RealFromWorkflowId abc
```

Output: 
```
{
    "Response": {
        "Data": true,
        "LinkId": "abc",
        "RequestId": "abc"
    }
}
```

**Example 2: 成功**

成功

Input: 

```
tccli wedata ModifyTaskLinksDs --cli-unfold-argument  \
    --ProjectId 1234 \
    --TaskFrom 123 \
    --TaskTo 123 \
    --LinkDependencyType 123 \
    --WorkflowId 123 \
    --RealFromWorkflowId 1234
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "Cannot deserialize value of type `com.tencent.tbds.guldan.api.store.service.api.utils.LinkDependencyType` from String \"123\": not one of the values accepted for Enum class: [non_normal_all_forward, non_normal_specific_one_backward, non_normal_specific_one_forward, non_normal_all_backward, normal_all, self, non_normal_first_one_backward, non_normal_any_one_forward, normal_last_one, non_normal_first_one_forward, normal_any_one, normal_first_one, non_normal_last_one_forward, normal_specific_one, non_normal_any_one_backward, non_normal_last_one_backward]\n at [Source: (org.springframework.util.StreamUtils$NonClosingInputStream); line: 1, column: 74] (through reference chain: com.tencent.tbds.datastudio.pojo.task.ModifyTaskLinksRequest[\"LinkDependencyType\"])"
        },
        "RequestId": "998c1f74-9a31-4971-aadf-5c8957d97653"
    }
}
```

