**Example 1: 修改拨测分组示例**



Input: 

```
tccli cat ModifyAgentGroup --cli-unfold-argument  \
    --GroupId 100004185 \
    --GroupName TestModifyAgentGroup \
    --IsDefault 0 \
    --Agents.0.Province gd \
    --Agents.0.Isp cmc
```

Output: 
```
{
    "Response": {
        "RequestId": "d515a0aa-9c67-4637-a955-5cbecbeae248"
    }
}
```

