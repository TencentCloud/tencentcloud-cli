**Example 1: CheckIntegrationNodeNameExists**

判断集成节点名称是否存在

Input: 

```
tccli wedata CheckIntegrationNodeNameExists --cli-unfold-argument  \
    --ProjectId xx \
    --Id 0 \
    --TaskId xx \
    --Name xx
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "xx"
    }
}
```

