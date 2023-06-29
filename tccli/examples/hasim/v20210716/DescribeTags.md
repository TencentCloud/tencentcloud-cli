**Example 1: 查询标签列表**

查询标签列表

Input: 

```
tccli hasim DescribeTags --cli-unfold-argument  \
    --Name demo
```

Output: 
```
{
    "Response": {
        "Data": {
            "Total": 0,
            "List": [
                {
                    "Comment": "xx",
                    "Name": "xx",
                    "UpdatedAt": "xx",
                    "ID": 0,
                    "CreatedAt": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

