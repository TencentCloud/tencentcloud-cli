**Example 1: 删除规则**

删除规则

Input: 

```
tccli cfw DeleteAcRule --cli-unfold-argument  \
    --Id 36069 \
    --Direction 1 \
    --EdgeId edge-ppt3pi01 \
    --Area ap-guangzhou
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Info": "success",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

