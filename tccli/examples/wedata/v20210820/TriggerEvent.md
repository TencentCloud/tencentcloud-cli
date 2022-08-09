**Example 1: 范例**



Input: 

```
tccli wedata TriggerEvent --cli-unfold-argument  \
    --ProjectId 1 \
    --Description 手动触发 \
    --Name mytest \
    --Dimension  20220729
```

Output: 
```
{
    "Response": {
        "RequestId": "a339e515-9f6c-46b1-a43a-587f1c39067c",
        "Data": {
            "Result": true,
            "ErrorId": null,
            "ErrorDesc": null
        }
    }
}
```

