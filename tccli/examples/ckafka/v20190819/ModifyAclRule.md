**Example 1: 修改ACL规则示范**

修改ACL规则示范

Input: 

```
tccli ckafka ModifyAclRule --cli-unfold-argument  \
    --InstanceId xxx \
    --RuleName xxx \
    --IsApplied 1
```

Output: 
```
{
    "Response": {
        "Result": 1,
        "RequestId": "72b987c9-8842-47ac-9ad6-fa2bde3e936d"
    }
}
```

