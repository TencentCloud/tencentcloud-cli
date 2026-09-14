**Example 1: 创建标签**

创建标签

Input: 

```
tccli adp CreateLabel --cli-unfold-argument  \
    --KbId 2097216771738716160 \
    --Name 班级 \
    --TermList.0.Term 二年级
```

Output: 
```
{
    "Response": {
        "LabelId": "2097217495989591744",
        "TermList": [
            {
                "TermId": "2097217495989591745",
                "Term": "二年级",
                "SynonymList": []
            }
        ],
        "RequestId": "df05caba-494f-491f-bf4a-3355233445b8"
    }
}
```

