**Example 1: 获取训练文本信息**

获取训练文本信息

Input: 

```
tccli vrs GetTrainingText --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "63f89e17a6f281d5108ab7b0",
        "Data": {
            "TrainingTextList": [
                {
                    "TextId": "00001",
                    "Text": "在很久很久以前 鸟群中有一只小鸟"
                },
                {
                    "TextId": "00005",
                    "Text": "那时候的凤凰还不是鸟中之王 只是一个很不起眼的小鸟"
                }
            ]
        }
    }
}
```

