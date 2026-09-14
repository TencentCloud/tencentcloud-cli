**Example 1: 修改标签**

修改标签

Input: 

```
tccli adp ModifyLabel --cli-unfold-argument  \
    --Fields.Name 测试33 \
    --Fields.TermModifyList.0.ModifyAction 1 \
    --Fields.TermModifyList.0.Term 323232 \
    --KbId 2095766521673516736 \
    --LabelId 2096808563606119109 \
    --UpdateMask.Paths Name
```

Output: 
```
{
    "Response": {
        "TermList": [
            {
                "TermId": "2098002223121287936",
                "Term": "323232",
                "SynonymList": []
            }
        ],
        "RequestId": "f83fcb3a-adfc-491a-9386-a95444c620d2"
    }
}
```

