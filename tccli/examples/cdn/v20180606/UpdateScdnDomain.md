**Example 1: SCDN域名配置变更**

SCDN域名配置变更

Input: 

```
tccli cdn UpdateScdnDomain --cli-unfold-argument  \
    --Domain www.test.com \
    --Acl.Switch on \
    --Acl.ScriptData.0.RuleName test \
    --Acl.ScriptData.0.Result refuse \
    --Acl.ScriptData.0.Configure.0.MatchKey params \
    --Acl.ScriptData.0.Configure.0.LogiOperator exclude \
    --Acl.ScriptData.0.Configure.0.MatchValue www.attatck.com
```

Output: 
```
{
    "Response": {
        "RequestId": "08b287d9-6342-4b70-9ec7-201efcd93b9d",
        "Result": "Success"
    }
}
```

