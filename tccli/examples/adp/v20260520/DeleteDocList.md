**Example 1: 批量删除文档**

批量删除文档

Input: 

```
tccli adp DeleteDocList --cli-unfold-argument  \
    --DocIdList 2097525829590848512 \
    --KbId 2095766521673516736
```

Output: 
```
{
    "Response": {
        "ResultList": [
            {
                "Id": "2097525829590848512",
                "Succeeded": true,
                "Reason": ""
            }
        ],
        "RequestId": "0b23fead-c4a3-41da-964a-92936fd22a62"
    }
}
```

