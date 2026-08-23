**Example 1: 查询镜像敏感信息列表**



Input: 

```
tccli csip DescribeImageSensitiveInfoList --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Filter.Filters.0.Name Id \
    --Filter.Filters.0.Values 802
```

Output: 
```
{
    "Response": {
        "SensitiveInfoList": [
            {
                "Behavior": 2,
                "Describe": "sensitive file zh",
                "ImageId": "802",
                "InstructionContent": "cat /etc/secret/bulk0530-token-0999414",
                "Level": 2,
                "OwnerAccountName": "70000*******",
                "OwnerAppId": 260000000,
                "OwnerUin": "70000*******",
                "Type": 114
            }
        ],
        "TotalCount": 1,
        "RequestId": "aa11082d-719a-48ac-833f-260460df9fc8"
    }
}
```

