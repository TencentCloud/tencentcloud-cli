**Example 1: CheckIntegrationNodeNameExists**

判断集成节点名称是否存在

Input: 

```
tccli wedata CheckIntegrationNodeNameExists --cli-unfold-argument  \
    --ProjectId abc \
    --Id 0 \
    --TaskId abc \
    --Name abc
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

