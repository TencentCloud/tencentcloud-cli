**Example 1: 修改单个 QA**

修改单个 QA

Input: 

```
tccli adp ModifyQA --cli-unfold-argument  \
    --Fields.Answer 333334 \
    --Fields.CategoryId 2085302048496970304 \
    --Fields.DocId 0 \
    --Fields.EffectiveDomain 2 \
    --Fields.ExpirationPolicy.EffectivePeriod.EndTime 0 \
    --Fields.ExpirationPolicy.ExpireBehavior 1 \
    --Fields.Question 测试一下2 \
    --Fields.QuestionDescription  \
    --KbId 2085302046444998912 \
    --QaId 2097209703376155200 \
    --UpdateMask.Paths category_id
```

Output: 
```
{
    "Response": {
        "RequestId": "7402c05e-ecaf-4799-af8d-ccf8933b9856"
    }
}
```

