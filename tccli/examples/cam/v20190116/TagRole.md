**Example 1: 角色绑定标签**



Input: 

```
tccli cam TagRole --cli-unfold-argument  \
    --Tags.0.Key AKey \
    --Tags.0.Value AValue \
    --RoleName CAM_QCSRole
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx-xxx-xxx"
    }
}
```

