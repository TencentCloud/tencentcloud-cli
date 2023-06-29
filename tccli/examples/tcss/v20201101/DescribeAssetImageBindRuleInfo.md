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
                "RuleId": "xx",
                "ScanTime": "xx",
                "ImageId": "xx",
                "ImageName": "xx",
                "RuleName": "xx",
                "ContainerCnt": 0
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

