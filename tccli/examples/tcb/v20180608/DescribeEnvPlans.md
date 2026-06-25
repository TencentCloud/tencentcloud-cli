**Example 1: 查询个人版套餐版本信息**

当需要获取可售卖的套餐信息，以用来调用CreateEnv等接口进行下单时

Input: 

```
tccli tcb DescribeEnvPlans --cli-unfold-argument  \
    --PackageId baas_personal
```

Output: 
```
{
    "Response": {
        "PlanList": [
            {
                "PackageDescription": "新手入门，高性价比",
                "PackageId": "baas_personal",
                "PackageTitle": "个人版",
                "PackageType": "default",
                "ResourceLimit": "{\"Qps\":500,\"InvokeNum\":{\"TimeUnit\":\"m\",\"Unit\":\"万次\",\"MaxSize\":20},\"Capacity\":{\"TimeUnit\":\"m\",\"Unit\":\"GB\",\"MaxSize\":3},\"Cdn\":{\"Flux\":{\"TimeUnit\":\"m\",\"Unit\":\"GB\",\"MaxSize\":10},\"BackFlux\":{\"TimeUnit\":\"m\",\"Unit\":\"GB\",\"MaxSize\":10}},\"Scf\":{\"Concurrency\":0,\"OutFlux\":{\"TimeUnit\":\"m\",\"Unit\":\"GB\",\"MaxSize\":4},\"MemoryUse\":{\"TimeUnit\":\"m\",\"Unit\":\"万GBS\",\"MaxSize\":15}},\"AI\":{\"Token\":{\"TimeUnit\":\"m\",\"Unit\":\"个\",\"MaxSize\":100000}},\"ResUse\":{\"MemoryUse\":{\"TimeUnit\":\"m\",\"Unit\":\"万CU\",\"MaxSize\":15}},\"Hosting\":{\"Capacity\":{\"TimeUnit\":\"m\",\"Unit\":\"GB\",\"MaxSize\":1}},\"APP\":{\"ReleaseAppNum\":{\"TimeUnit\":\"m\",\"Unit\":\"个\",\"MaxSize\":3}},\"Auth\":{\"UserNum\":{\"TimeUnit\":\"m\",\"Unit\":\"百\",\"MaxSize\":2}},\"Credits\":{\"TimeUnit\":\"m\",\"Unit\":\"个\",\"MaxSize\":\"40000\"}}",
                "UnitPrice": "39.9"
            }
        ],
        "RequestId": "95e8f5b1-a591-481c-a73f-5eee45abea04"
    }
}
```

