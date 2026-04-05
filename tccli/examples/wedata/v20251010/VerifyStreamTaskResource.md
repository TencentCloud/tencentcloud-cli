**Example 1: 示例1**



Input: 

```
tccli wedata VerifyStreamTaskResource --cli-unfold-argument  \
    --WorkspaceId 17663856806379896 \
    --TaskId ta-ad218e6d \
    --TaskVersion tv-c54d0523
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": "{\"EXECUTOR_GROUP_ALLOWANCE_CHECK\":{\"Status\":4,\"Result\":{\"executor_group_allowance\":\"任务未发布，无生产版本: ta-ad218e6d\"}},\"EXECUTOR_GROUP_STATUS_CHECK\":{\"Status\":4,\"Result\":{\"executor_group_status\":\"任务未发布，无生产版本: ta-ad218e6d\"}}}"
        },
        "RequestId": "45a67bd0-adcf-4609-8b00-333e89003fcb"
    }
}
```

