**Example 1: 创建边缘函数规则命中规则后执行指定函数**

为站点 zone-293e7s5jne1i 创建一个边缘函数规则，当请求host为 www.function.com 时命中规则，采用 direct（直接指定）的方式选择目标函数，目标函数 ID 为 ef-1pakhnuy 。

Input: 

```
tccli teo CreateFunctionRule --cli-unfold-argument  \
    --ZoneId zone-293e7s5jne1i \
    --FunctionRuleConditions.0.RuleConditions.0.Operator equal \
    --FunctionRuleConditions.0.RuleConditions.0.Values www.function.com \
    --FunctionRuleConditions.0.RuleConditions.0.Target host \
    --TriggerType direct \
    --FunctionId ef-1pakhnuy \
    --Remark function rule trigger direct
```

Output: 
```
{
    "Response": {
        "RuleId": "rule-vnqup0uc",
        "RequestId": "aab9a28a-4cce-434d-852f-5442275817aa"
    }
}
```

**Example 2: 创建边缘函数规则命中规则后根据客户请求地区执行不同的函数**

为站点 zone-293e7s5jne1i 创建一个边缘函数规则，当请求host为 www.function.com 时命中规则，采用 region（基于客户端 IP 国家/地区）的方式选择目标函数，如果客户端的 IP 归属地为中国大陆，则执行函数 ef-1pakhnuy ，如果客户端的 IP 归属地为其他地区，则执行函数 ef-1wekxwnu 。

Input: 

```
tccli teo CreateFunctionRule --cli-unfold-argument  \
    --ZoneId zone-293e7s5jne1i \
    --FunctionRuleConditions.0.RuleConditions.0.Operator equal \
    --FunctionRuleConditions.0.RuleConditions.0.Values www.function.com \
    --FunctionRuleConditions.0.RuleConditions.0.Target host \
    --TriggerType region \
    --RegionMappingSelections.0.FunctionId ef-1pakhnuy \
    --RegionMappingSelections.0.Regions CN \
    --RegionMappingSelections.1.FunctionId ef-1wekxwnu \
    --RegionMappingSelections.1.Regions Default \
    --Remark function rule trigger region
```

Output: 
```
{
    "Response": {
        "RuleId": "rule-vnqup0uc",
        "RequestId": "aab9a28a-4cce-434d-852f-5442275817aa"
    }
}
```

**Example 3: 创建边缘函数规则命中规则后根据客户设置的权重执行不同的函数**

为站点 zone-293e7s5jne1i 创建一个边缘函数规则，当请求host为 www.function.com 时命中规则，采用 weight（基于权重）的方式选择目标函数，有20%的概率，执行函数 ef-1pakhnuy ，有80%的概率，执行函数 ef-1wekxwnu 。

Input: 

```
tccli teo CreateFunctionRule --cli-unfold-argument  \
    --ZoneId zone-293e7s5jne1i \
    --FunctionRuleConditions.0.RuleConditions.0.Operator equal \
    --FunctionRuleConditions.0.RuleConditions.0.Values www.function.com \
    --FunctionRuleConditions.0.RuleConditions.0.Target host \
    --TriggerType weight \
    --WeightedSelections.0.FunctionId ef-1wekxwnu \
    --WeightedSelections.0.Weight 80 \
    --WeightedSelections.1.FunctionId ef-1pakhnuy \
    --WeightedSelections.1.Weight 20 \
    --Remark function rule trigger weight
```

Output: 
```
{
    "Response": {
        "RuleId": "rule-vnqup0uc",
        "RequestId": "aab9a28a-4cce-434d-852f-5442275817aa"
    }
}
```

