**Example 1: 删除事件监听者**

删除事件监听者

Input: 

```
tccli wedata DeleteDsEventListener --cli-unfold-argument  \
    --ProjectId abc \
    --Key abc \
    --Type abc \
    --EventProjectId abc \
    --EventName abc
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "abc"
    }
}
```

