**Example 1: 问药测试**



Input: 

```
tccli ig GetLLMDiagnosisDrugChat --cli-unfold-argument  \
    --PartnerId 1*******4 \
    --PartnerSecret **************a36bbdd17960b3d70e \
    --HospitalAppId ******38323 \
    --DialogueId 74836139-f2ca-4aba-b7de-47705aefafbd \
    --Message 阿莫西林的适应症 \
    --ResultType 0
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Message": "success",
        "RequestId": "0766ff4a-3eda-434c-a749-f13a93658f44",
        "Data": {
            "Content": "【阿莫西林】是一款【β-内酰胺类抗生素（青霉素类）】，主要用于***",
            "Think": "",
            "Sort": 0,
            "IsFinish": true,
            "IsSensitive": false,
            "GuessQuestions": [
                {
                    "Title": "阿莫西林和头孢有什么区别？  "
                },
                {
                    "Title": "服用阿莫西林会过敏吗？  "
                },
                {
                    "Title": "阿莫西林饭前吃还是饭后吃？"
                }
            ],
            "HighlightWords": []
        }
    }
}
```

