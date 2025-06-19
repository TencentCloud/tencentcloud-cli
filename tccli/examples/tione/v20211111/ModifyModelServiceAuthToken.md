**Example 1: 修改示例**

修改一个 token

Input: 

```
tccli tione ModifyModelServiceAuthToken --cli-unfold-argument  \
    --ServiceGroupId ms-n2f929h2 \
    --NeedReset False \
    --AuthToken.Base.Value MTc0NDgwMjgxMTU \
    --AuthToken.Base.Name test \
    --AuthToken.Base.Description desc \
    --AuthToken.Base.CreateTime 2025-04-16T11:26:51Z \
    --AuthToken.Base.Status Enabled
```

Output: 
```
{
    "Response": {
        "RequestId": "71d3ba29-c044-4142-91c4-777c8fcec877"
    }
}
```

