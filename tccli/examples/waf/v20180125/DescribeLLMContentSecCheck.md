**Example 1: 测试用例**



Input: 

```
tccli waf DescribeLLMContentSecCheck --cli-unfold-argument  \
    --ServiceId 9000002887 \
    --Content *** \
    --Type 1 \
    --InstanceId waf_2l15cfe009ya8lg3 \
    --UserId 700002174132 \
    --TokenUsage 10000
```

Output: 
```
{
    "Response": {
        "Data": {
            "Action": "deny",
            "KeyWordsResult": [
                {
                    "Id": "politics_high",
                    "Name": "涉政-高敏感"
                }
            ],
            "Payload": "风险类型:内置关键词库-涉政-高敏感,风险内容:胡海峰",
            "RuleId": "5100000000",
            "RuleName": "关键词库检测"
        },
        "RequestId": "badc7789-41d7-44b9-84e3-38efd8d833d8"
    }
}
```

