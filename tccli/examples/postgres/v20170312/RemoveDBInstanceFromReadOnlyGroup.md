**Example 1: 用户将实例从只读组中移除**



Input: 

```
tccli postgres RemoveDBInstanceFromReadOnlyGroup --cli-unfold-argument  \
    --ReadOnlyGroupId "pgrogrp-k95qzetn" \
    --DBInstanceId "pgro-k95qzetn"
```

Output: 
```
{
    "Response": {
        "RequestId": "d43b2a9f-070c-480b-a0bb-7c210428cfe8",
        "FlowId": 912
    }
}
```

