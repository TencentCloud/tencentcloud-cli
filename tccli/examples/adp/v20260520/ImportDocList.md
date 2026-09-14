**Example 1: 批量导入文档**

批量导入文档

Input: 

```
tccli adp ImportDocList --cli-unfold-argument  \
    --DocList.0.FileId 2079463384883903552 \
    --KbId 2079089760838256704
```

Output: 
```
{
    "Response": {
        "ResultList": [
            {
                "Id": "2079876913604708608",
                "Reason": "",
                "Succeeded": true
            }
        ],
        "RequestId": "33ac60aa-d82f-4f2c-9f0b-71913caaf740"
    }
}
```

