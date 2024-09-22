**Example 1: 查询知识库容量饼图**

查询知识库容量饼图

Input: 

```
tccli lke DescribeKnowledgeUsagePieGraph --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AvailableCharSize": "10000000",
        "List": [
            {
                "AppName": "未使用",
                "Proportion": 0.9953504,
                "UsedCharSize": "9953504"
            },
            {
                "AppName": "企点智能客服02",
                "Proportion": 0.0016738,
                "UsedCharSize": "16738"
            },
            {
                "AppName": "测试下",
                "Proportion": 0.0016717,
                "UsedCharSize": "16717"
            },
            {
                "AppName": "无情三刀",
                "Proportion": 0.0013041,
                "UsedCharSize": "13041"
            }
        ],
        "RequestId": "19cfafe1-489d-40e8-b79f-dc9919ce3ccd"
    }
}
```

