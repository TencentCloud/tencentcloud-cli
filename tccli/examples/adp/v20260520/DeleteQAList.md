**Example 1: 批量删除 QA**

批量删除 QA

Input: 

```
tccli adp DeleteQAList --cli-unfold-argument  \
    --KbId 2097596899749103296 \
    --QaIdList 2097597073372212992
```

Output: 
```
{
    "Response": {
        "ResultList": [
            {
                "Id": "2097597073372212992",
                "Succeeded": true,
                "Reason": ""
            }
        ],
        "RequestId": "eb095262-d0cb-4988-b193-24fcebceea4c"
    }
}
```

