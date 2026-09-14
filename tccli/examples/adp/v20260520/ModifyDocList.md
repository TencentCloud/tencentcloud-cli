**Example 1: 批量修改文档**

批量修改文档

Input: 

```
tccli adp ModifyDocList --cli-unfold-argument  \
    --DocIdList 2096882953701315136 \
    --EffectiveDomain 4 \
    --KbId 2096881888856621696
```

Output: 
```
{
    "Response": {
        "ResultList": [
            {
                "Id": "2096882953701315136",
                "Succeeded": false,
                "Reason": "type:business, code:450156, msg:ErrDocNotAllowEdit"
            }
        ],
        "RequestId": "07edd952-9922-4f3e-8af5-13fc4afd6c25"
    }
}
```

