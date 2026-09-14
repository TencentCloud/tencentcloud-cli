**Example 1: 批量创建 QA**

批量创建 QA

Input: 

```
tccli adp CreateQAList --cli-unfold-argument  \
    --KbId 2057747189113440256 \
    --QaList.0.Question 苹果有多少个品种？ \
    --QaList.0.Answer 苹果大约有7500个品种 \
    --QaList.0.EffectiveDomain 4
```

Output: 
```
{
    "Response": {
        "ResultList": [
            {
                "Id": "2097886214516234688",
                "Succeeded": true,
                "Reason": ""
            }
        ],
        "RequestId": "bb39c555-1128-4ef0-85c6-dd76d7d9f00d"
    }
}
```

