**Example 1: 批量修改 QA**

批量修改 QA

Input: 

```
tccli adp ModifyQAList --cli-unfold-argument  \
    --KbId 2097635494119704256 \
    --QaIdList 2097635721520180864 \
    --EffectiveDomain 2 \
    --LabelRefList.ItemList.0.LabelId 2097635499087851136 \
    --LabelRefList.ItemList.0.LabelTermIdList 2097635499087851138
```

Output: 
```
{
    "Response": {
        "ResultList": [
            {
                "Id": "2097635721520180864",
                "Succeeded": true,
                "Reason": ""
            }
        ],
        "RequestId": "0685d2df-ea42-40ff-880f-7d00aa6a9e0e"
    }
}
```

