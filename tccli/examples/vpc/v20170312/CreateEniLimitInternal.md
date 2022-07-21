**Example 1: 添加ENI限制**



Input: 

```
tccli vpc CreateEniLimitInternal --cli-unfold-argument  \
    --EniLimitRequestSet.0.Owner 251198225 \
    --EniLimitRequestSet.0.InstanceId ins-y5gh3gq8 \
    --EniLimitRequestSet.0.Type 1 \
    --EniLimitRequestSet.0.Val 3 \
    --EniLimitRequestSet.0.LowerCpu 2 \
    --EniLimitRequestSet.0.UpperCpu 4 \
    --EniLimitRequestSet.0.LowerMem 1 \
    --EniLimitRequestSet.0.UpperMem 3
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

