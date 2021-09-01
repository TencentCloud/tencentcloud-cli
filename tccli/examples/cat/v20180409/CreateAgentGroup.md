**Example 1: 添加拨测分组示例**



Input: 

```
tccli cat CreateAgentGroup --cli-unfold-argument  \
    --GroupName test_group2 \
    --IsDefault 0 \
    --Agents.0.Province gd \
    --Agents.0.Isp cmc \
    --Agents.1.Province gd \
    --Agents.1.Isp cuc
```

Output: 
```
{
    "Response": {
        "GroupId": 28330
    }
}
```

