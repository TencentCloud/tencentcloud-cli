**Example 1: 注册云服务器到TCP监听器上**



Input: 

```
tccli clb RegisterTargets --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0 \
    --ListenerId lbl-d1ubsydq \
    --Targets.0.InstanceId ins-dm4xtz0i \
    --Targets.0.Port 233 \
    --Targets.0.Weight 10
```

Output: 
```
{
    "Response": {
        "RequestId": "898b431c-2745-4b27-80f6-e6e8038a0683"
    }
}
```

**Example 2: 注册云服务器到HTTP监听器的转发规则上（使用LocationId指定规则）**



Input: 

```
tccli clb RegisterTargets --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0 \
    --ListenerId lbl-4fbxq45k \
    --LocationId loc-r2q3jd4c \
    --Targets.0.InstanceId ins-dm4xtz0i \
    --Targets.0.Port 334 \
    --Targets.0.Weight 10
```

Output: 
```
{
    "Response": {
        "RequestId": "d4846a22-e758-407f-a526-db3f2d37d00e"
    }
}
```

**Example 3: 注册云服务器到HTTP监听器的转发规则上（使用Domain和Url指定规则）**



Input: 

```
tccli clb RegisterTargets --cli-unfold-argument  \
    --LoadBalancerId lb-cuxw2rm0 \
    --ListenerId lbl-4fbxq45k \
    --Domain foo.net \
    --Url /bar8 \
    --Targets.0.InstanceId ins-dm4xtz0i \
    --Targets.0.Port 233 \
    --Targets.0.Weight 10
```

Output: 
```
{
    "Response": {
        "RequestId": "11b4338f-2d00-4766-bc67-581d959b3488"
    }
}
```

