**Example 1: 查询mcp server唯一性**

查询mcp server唯一性

Input: 

```
tccli apis CheckMcpServerUnique --cli-unfold-argument  \
    --InstanceID ins-9c4a1db3 \
    --Field name \
    --Value hh \
    --ID 
```

Output: 
```
{
    "Response": {
        "Data": {
            "IsConflict": false,
            "Message": ""
        },
        "RequestId": "3fcd8e59-0c84-434e-9f07-9091f1de997d"
    }
}
```

