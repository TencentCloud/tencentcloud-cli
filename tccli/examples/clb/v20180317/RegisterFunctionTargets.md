**Example 1: 绑定云函数到转发规则上**

将一个云函数绑定到负载均衡实例的7层转发规则上。

Input: 

```
tccli clb RegisterFunctionTargets --cli-unfold-argument  \
    --LocationId loc-abcd1234 \
    --ListenerId lbl-d1ub**** \
    --FunctionTargets.0.Function.FunctionNamespace ns_test \
    --FunctionTargets.0.Function.FunctionName name_test \
    --FunctionTargets.0.Function.FunctionQualifier version_test \
    --FunctionTargets.0.Weight 66 \
    --LoadBalancerId lb-cuxw****
```

Output: 
```
{
    "Response": {
        "RequestId": "11b4338f-2d00-4766-bc67-581d959b3488"
    }
}
```

