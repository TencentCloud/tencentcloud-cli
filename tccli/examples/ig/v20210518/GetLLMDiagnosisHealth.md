**Example 1: 症状自查测试**



Input: 

```
tccli ig GetLLMDiagnosisHealth --cli-unfold-argument  \
    --PartnerId 1*******4 \
    --PartnerSecret **************a36bbdd17960b3d70e \
    --HospitalAppId ******38323 \
    --DialogueId 74836139-f2ca-4aba-b7de-47705aefafbd \
    --Message 有点头痛 \
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
            "Content": "头痛多久了",
            "Think": "",
            "Sort": 0,
            "IsFinish": true,
            "IsSensitive": false,
            "GuessQuestions": [],
            "HighlightWords": []
        }
    }
}
```

