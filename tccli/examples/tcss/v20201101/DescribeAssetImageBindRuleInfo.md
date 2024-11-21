**Example 1: 镜像绑定规则列表**



Input: 

```
tccli tcss DescribeAssetImageBindRuleInfo --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ImageBindRuleSet": [
            {
                "ImageSize": 0,
                "RuleId": "10001",
                "ScanTime": "2022-01-1 00:00:00",
                "ImageId": "image-id",
                "ImageName": "image-name",
                "RuleName": "rule_name",
                "ContainerCnt": 0
            }
        ],
        "TotalCount": 1,
        "RequestId": "8bc803fd-d85d-47b8-9e2b-9644674be677"
    }
}
```

