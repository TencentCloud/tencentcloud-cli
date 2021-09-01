**Example 1: 只读组内实例流量重新负载**



Input: 

```
tccli postgres RebalanceReadOnlyGroup --cli-unfold-argument  \
    --ReadOnlyGroupId "pgrogrp-e0tfm161"
```

Output: 
```
{
    "Response": {
        "RequestId": "d43b2a9f-070c-480b-a0bb-7c210428cfe8"
    }
}
```

