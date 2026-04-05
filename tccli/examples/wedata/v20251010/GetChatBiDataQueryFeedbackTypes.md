**Example 1: 查询反馈类型列表**



Input: 

```
tccli wedata GetChatBiDataQueryFeedbackTypes --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "SubType": "日期/时间错误",
                    "Type": "结果"
                },
                {
                    "SubType": "结果值不对",
                    "Type": "结果"
                },
                {
                    "SubType": "缺少列或者行",
                    "Type": "结果"
                },
                {
                    "SubType": "知识理解错误",
                    "Type": "结果"
                },
                {
                    "SubType": "行数过多",
                    "Type": "结果"
                },
                {
                    "SubType": "类型不合适",
                    "Type": "可视化"
                },
                {
                    "SubType": "条图",
                    "Type": "期待的可视化类型"
                },
                {
                    "SubType": "线图",
                    "Type": "期待的可视化类型"
                },
                {
                    "SubType": "饼图",
                    "Type": "期待的可视化类型"
                }
            ]
        },
        "RequestId": "6957fefe-1bc9-4fee-bc51-1e91b6ce2a6c"
    }
}
```

