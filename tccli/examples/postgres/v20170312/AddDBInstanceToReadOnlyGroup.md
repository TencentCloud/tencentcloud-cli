**Example 1: 将实例postgres-k95qzetn加入只读组pgrogrp-test中**



Input: 

```
tccli postgres AddDBInstanceToReadOnlyGroup --cli-unfold-argument  \
    --ReadOnlyGroupId "pgrogrp-test" \
    --DBInstanceId "postgres-k95qzetn"
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

