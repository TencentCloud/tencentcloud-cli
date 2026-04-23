**Example 1: CreateSignOnAgentService**



Input: 

```
tccli apis CreateSignOnAgentService --cli-unfold-argument  \
    --InstanceID ins-******** \
    --AgentID ins-******** \
    --IP 127.0.0.1 \
    --Port 1234 \
    --AgentToken token123 \
    --Path /test \
    --BaseDomain test.com \
    --AllowedUsers user123
```

Output: 
```
{
    "Response": {
        "RequestId": "c717c4f0-9ddc-4174-8343-0b32bd2c2430"
    }
}
```

