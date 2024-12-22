**Example 1: 修改内容标识符描述**

将 eocontent-27q0p0bbli16 的内容标识符的描述修改为 content-new。

Input: 

```
tccli teo ModifyContentIdentifier --cli-unfold-argument  \
    --ContentId eocontent-27q0p0bbli16 \
    --Description content-new
```

Output: 
```
{
    "Response": {
        "RequestId": "3b140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

