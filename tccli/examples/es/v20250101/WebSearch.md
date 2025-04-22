**Example 1: 联网搜索**

用户需要搜索 2025 年货币政策相关的网页内容，并指定来源为政府网站。

Input: 

```
tccli es WebSearch --cli-unfold-argument  \
    --Query 2025年货币政策有哪些变化？ \
    --Count 20 \
    --Site gov.cn \
    --FetchContent False \
    --StartTime 1704038400 \
    --EndTime 1712592000 \
    --SearchEngine sogou
```

Output: 
```
{
    "Response": {
        "RequestId": "21739985-c9bf-4add-998b-7c5b055b3289",
        "Query": "2025年货币政策有哪些变化？",
        "Status": "completed",
        "SearchEngine": "sogou",
        "Results": [
            {
                "Title": "2025年政府财政改革报告",
                "Url": "www.example.gov.cn",
                "Summary": "2025年财政改革措施为...",
                "Time": "2025年4月9日"
            }
        ]
    }
}
```

