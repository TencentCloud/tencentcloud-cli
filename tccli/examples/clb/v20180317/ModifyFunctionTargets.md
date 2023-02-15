**Example 1: 修改负载均衡转发规则上所绑定的云函数。**



Input: 

```
tccli clb ModifyFunctionTargets --cli-unfold-argument  \
    --LocationId loc-xxxxxxxx \
    --ListenerId lbl-xxxxxxxx \
    --FunctionTargets.0.Function.FunctionNamespace ns_test \
    --FunctionTargets.0.Function.FunctionName name_test \
    --FunctionTargets.0.Function.FunctionQualifier version_test \
    --FunctionTargets.0.Weight 66 \
    --LoadBalancerId lb-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "85c7b3e8-7fd8-4c62-8b3b-7ba52d7a1dca"
    }
}
```

