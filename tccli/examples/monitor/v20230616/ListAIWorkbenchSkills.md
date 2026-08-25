**Example 1: Mock返回示例**



Input: 

```
tccli monitor ListAIWorkbenchSkills --cli-unfold-argument  \
    --PerPage 100 \
    --PageNo 1 \
    --SkillIds skl-********
```

Output: 
```
{
    "Response": {
        "PageResult": {
            "CurrentPageNo": 1,
            "TotalCount": 5,
            "TotalPage": 1
        },
        "Skills": [
            {
                "Description": "解析PDF/Word/Excel文件并提取文本内容",
                "Enabled": true,
                "Name": "文件解析",
                "SkillId": "skill-cust-file-parser-002"
            }
        ],
        "RequestId": "c05cd8e1-89a7-4260-a07e-a8047be55a45"
    }
}
```

