**Example 1: 修改指定认证选项内容**

修改某个已有的认证选项内容。

Input: 

```
tccli teo ModifySecurityClientAttester --cli-unfold-argument  \
    --ZoneId zone-12ekfafefe3 \
    --ClientAttesters.0.Name test \
    --ClientAttesters.0.Id attest-2180012392 \
    --ClientAttesters.0.AttesterSource TC-RCE \
    --ClientAttesters.0.TCRCEOption.Channel 12399223 \
    --ClientAttesters.0.AttesterDuration 300s
```

Output: 
```
{
    "Response": {
        "RequestId": "ddf831fc-cf45-40fe-81b0-2d9cdd4c1bd6"
    }
}
```

