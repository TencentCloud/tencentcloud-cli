**Example 1: ModifyDBInstanceReadOnlyGroup**



Input: 

```
tccli postgres ModifyDBInstanceReadOnlyGroup --cli-unfold-argument  \
    --NewReadOnlyGroupId pgrogrp-nqwpkjbu \
    --ReadOnlyGroupId pgrogrp-mnwtmp20 \
    --DBInstanceId pgro-k95qzetn
```

Output: 
```
{
    "Response": {
        "RequestId": "d43b2a9f-070c-480b-a0bb-7c210428cfe8",
        "FlowId": 912,
        "TaskId": 912
    }
}
```

