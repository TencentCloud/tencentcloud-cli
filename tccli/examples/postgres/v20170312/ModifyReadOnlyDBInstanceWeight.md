**Example 1: ModifyReadOnlyDBInstanceWeight**



Input: 

```
tccli postgres ModifyReadOnlyDBInstanceWeight --cli-unfold-argument  \
    --ReadOnlyGroupId pgrogp-test \
    --DBInstanceId pgro-e0tfm161 \
    --Weight 1
```

Output: 
```
{
    "Response": {
        "RequestId": "d43b2a9f-070c-480b-a0bb-7c210428cfe8"
    }
}
```

