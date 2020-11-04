**Example 1: 修改资源关联的标签值**



Input: 

```
tccli tag UpdateResourceTagValue --cli-unfold-argument  \
    --TagKey testTagKey\
    --TagValue testTagValue\
    --Resource qcs::cvm:ap-beijing:uin/1234567:instance/ins-123
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

