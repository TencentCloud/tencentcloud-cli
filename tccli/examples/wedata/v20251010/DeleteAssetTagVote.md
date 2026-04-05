**Example 1: 删除资产打标信息**

删除资产打标信息

Input: 

```
tccli wedata DeleteAssetTagVote --cli-unfold-argument  \
    --PropertyType catalog \
    --PropertyId 566
```

Output: 
```
{
    "Response": {
        "Data": {
            "Message": "删除成功",
            "Success": true
        },
        "RequestId": "aa0c4463-737b-4e71-9506-3f9cfcf0cb55"
    }
}
```

