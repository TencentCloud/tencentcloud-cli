**Example 1: API调用**



Input: 

```
tccli tmt ImageTranslate --cli-unfold-argument  \
    --Target en \
    --SessionUuid session-00001 \
    --ProjectId 0 \
    --Scene doc \
    --Source zh \
    --Data iVBORw0KGgoAAAANSUhEUgAAAdkAAABPCAYAAACnD7%252FoAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAJ
......
CCyAAAAwCQgsgAAAMAkILIAAADAJCCyAAAAwCQgsgAAAMAkILIAAADAFJblX8%252F8oMOWYN6nAAAAAElFTkSuQmCC
```

Output: 
```
{
    "Response": {
        "ImageRecord": {
            "Value": [
                {
                    "H": 21,
                    "SourceText": " 我们可以比较容易的将字典(ict)类型转为字符串(string)类型。",
                    "TargetText": "We can easily convert the dictionary icttype to the string) type.",
                    "W": 373,
                    "X": 12,
                    "Y": 53
                }
            ]
        },
        "Source": "zh",
        "Target": "en",
        "SessionUuid": "session-00001",
        "RequestId": "6e698139-615a-4d42-8dea-6bfada24e83c"
    }
}
```

