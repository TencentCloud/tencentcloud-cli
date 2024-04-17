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

**Example 2: 触发事件**

触发事件

Input: 

```
tccli wedata TriggerEvent --cli-unfold-argument  \
    --ProjectId 1492511691706699776 \
    --Name test_event_2 \
    --Dimension 20240411 \
    --Description "手动触发"
```

Output: 
```
{
    "Response": {
        "Data": {
            "ErrorDesc": null,
            "ErrorId": null,
            "Result": true
        },
        "RequestId": "5f569dca-2f3a-4e57-93ac-449e787e0955"
    }
}
```

