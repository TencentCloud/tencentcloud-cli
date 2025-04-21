**Example 1: 批量校验资源合法性**

批量校验资源合法性

Input: 

```
tccli ioa CheckBusinessResources --cli-unfold-argument  \
    --URL abc \
    --SheetName abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TaskID": "abc"
        },
        "RequestId": "abc"
    }
}
```

