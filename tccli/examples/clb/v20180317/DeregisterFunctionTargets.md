**Example 1: 将云函数从转发规则上解绑**

将一个云函数从负载均衡的转发规则上解绑。

Input: 

```
tccli clb DeregisterFunctionTargets --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0 \
    --ListenerId lbl-d1ubsydq \
    --LocationId loc-abcd1234 \
    --FunctionTargets.0.Weight 66 \
    --FunctionTargets.0.Function.FunctionNamespace ns_test \
    --FunctionTargets.0.Function.FunctionName name_test \
    --FunctionTargets.0.Function.FunctionQualifier version_test
```

Output: 
```
{
    "Response": {
        "RequestId": "11b4338f-2d00-4766-bc67-581d959b3488"
    }
}
```

