**Example 1: 批量删除标签**

批量删除标签

Input: 

```
tccli adp DeleteLabelList --cli-unfold-argument  \
    --KbId 2095766521673516736 \
    --LabelIdList 2096808563606119107
```

Output: 
```
{
    "Response": {
        "ResultList": [
            {
                "Id": "2096808563606119107",
                "Succeeded": true,
                "Reason": ""
            }
        ],
        "RequestId": "b83c3494-3da7-4604-b31b-94714736ff76"
    }
}
```

