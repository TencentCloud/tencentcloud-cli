**Example 1: 查询 AI 通话内容提取结果示例**

查询 AI 通话内容提取结果示例

Input: 

```
tccli ccc DescribeAICallExtractResult --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --SessionId adcf61b8-dbb9-4c20-87bf-c0744c04bade \
    --StartTime 1737350008 \
    --EndTime 1737356008
```

Output: 
```
{
    "Response": {
        "RequestId": "6bb56a09-2787-40bc-80c5-dc6dab783eff",
        "ResultList": [
            {
                "InfoType": "Boolean",
                "InfoName": "兴趣",
                "InfoContent": "用户是否对产品感兴趣",
                "Result": {
                    "Text": "",
                    "Chosen": [],
                    "Boolean": true,
                    "Number": 0
                }
            }
        ]
    }
}
```

