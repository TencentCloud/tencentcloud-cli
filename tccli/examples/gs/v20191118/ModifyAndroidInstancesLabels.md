**Example 1: 示例**

示例

Input: 

```
tccli gs ModifyAndroidInstancesLabels --cli-unfold-argument  \
    --AndroidInstanceIds cai-251006279-ea99cM7rbg6 cai-251006279-ea993NPwvHN \
    --AndroidInstanceLabels.0.Key key1 \
    --AndroidInstanceLabels.0.Value value1 \
    --AndroidInstanceLabels.1.Key key2 \
    --AndroidInstanceLabels.1.Value value2 \
    --AndroidInstanceLabels.2.Key key3 \
    --AndroidInstanceLabels.2.Value value3 \
    --Operation ADD
```

Output: 
```
{
    "Response": {
        "RequestId": "fe0851d4-fda2-4d73-9efc-9952971b611c"
    }
}
```

