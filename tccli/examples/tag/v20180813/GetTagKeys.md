**Example 1: 查询标签键列表**



Input: 

```
tccli tag GetTagKeys --cli-unfold-argument  \
    --PaginationToken oaWvQ5SFPGhUtWMA3LKTKgryBtKrDB215AUhaE********** \
    --MaxResults 10
```

Output: 
```
{
    "Response": {
        "PaginationToken": "kF-AjkqVQoB_9GwaBebsjvXudAjBadBTakA1WqPbwR66KjGE0INYQhQ**********",
        "TagKeys": [
            "testKey1",
            "testKey2"
        ],
        "RequestId": "104eeaa2-c268-43e5-b073-0fade*******"
    }
}
```

