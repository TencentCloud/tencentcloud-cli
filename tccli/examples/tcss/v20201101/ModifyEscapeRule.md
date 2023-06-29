**Example 1: updataEscape**



Input: 

```
tccli tcss ModifyEscapeRule --cli-unfold-argument  \
    --RuleSet.0.Type "ESCAPE_HOST_ACESS_FILE" \
    --RuleSet.0.IsEnable true \
    --RuleSet.1.Type "ESCAPE_MOUNT_NAMESPACE" \
    --RuleSet.1.IsEnable true \
    --RuleSet.2.Type "ESCAPE_PRIVILEDGE" \
    --RuleSet.2.IsEnable true \
    --RuleSet.3.Type "ESCAPE_PRIVILEDGE_CONTAINER_START" \
    --RuleSet.3.IsEnable true \
    --RuleSet.4.Type "ESCAPE_MOUNT_SENSITIVE_PTAH" \
    --RuleSet.4.IsEnable true \
    --RuleSet.5.Type "ESCAPE_SYSCALL" \
    --RuleSet.5.IsEnable true
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

