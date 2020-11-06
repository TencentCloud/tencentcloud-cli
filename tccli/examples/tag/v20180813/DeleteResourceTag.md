**Example 1: 标签解绑资源**



Input: 

```
tccli tag DeleteResourceTag --cli-unfold-argument  \
    --TagKey testTagKey \
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

