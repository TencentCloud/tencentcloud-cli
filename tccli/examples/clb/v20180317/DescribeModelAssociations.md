**Example 1: 默认查询模型路由**



Input: 

```
tccli clb DescribeModelAssociations --cli-unfold-argument  \
    --ModelRouterId cmr-mo1nqzs5
```

Output: 
```
{
    "Response": {
        "ModelAssociationSet": [],
        "ModelRouterId": "cmr-mo1nqzs5",
        "TotalCount": 0,
        "RequestId": "ae6af60d-9352-4e66-bc81-7ffb1d31abcc"
    }
}
```

**Example 2: 查询已绑定可调度模型的模型路由实例详情**

查询已绑定可调度模型的模型路由实例详情

Input: 

```
tccli clb DescribeModelAssociations --cli-unfold-argument  \
    --ModelRouterId cmr-mwmjm160
```

Output: 
```
{
    "Response": {
        "ModelAssociationSet": [
            {
                "InputModalitiesUnion": [
                    "text"
                ],
                "ModelName": "claude-Opus-4.8",
                "ServiceProviders": [
                    {
                        "AccessType": "PublicCustom",
                        "AssociationStatus": "Active",
                        "InputModalities": [
                            "text"
                        ],
                        "Order": 1,
                        "Protocol": "anthropic",
                        "Provider": "anthropic",
                        "ServiceProviderId": "byok-fcf1iehy",
                        "ServiceProviderName": "test-claude",
                        "Weight": 30
                    }
                ],
                "Type": "BYOK"
            }
        ],
        "ModelRouterId": "cmr-mwmjm160",
        "TotalCount": 2,
        "RequestId": "34b80df0-61f8-40fe-9624-9dfe1250ce38"
    }
}
```

