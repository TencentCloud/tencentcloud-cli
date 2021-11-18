**Example 1: 创建一个分析项**



Input: 

```
tccli bsca CreateAnalysis --cli-unfold-argument  \
    --AnalysisName MyAnalysis \
    --AnalysisType GENERIC \
    --FileName demo.img \
    --FileTicketId 1234567890-716cc6c7-f60c-4e08-9f91-e3e3b73144e2
```

Output: 
```
{
    "Response": {
        "AnalysisId": "4a49ab59-cea9-4d19-bed3-326a27465d92",
        "RequestId": "eacfb401-a322-493a-8e36-83b295412345"
    }
}
```

