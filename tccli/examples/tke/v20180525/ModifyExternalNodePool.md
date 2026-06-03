**Example 1: 修改注册节点池**

修改注册节点池

Input: 

```
tccli tke ModifyExternalNodePool --cli-unfold-argument  \
    --ClusterId cls-lm91rql0 \
    --NodePoolId np-kennkdng \
    --Name IDC节点池Modified \
    --Labels.0.Name lkong1modify \
    --Labels.0.Value lkong1modify \
    --Labels.1.Name tke.cloud.tencent.com/location \
    --Labels.1.Value gz
```

Output: 
```
{
    "Response": {
        "RequestId": "1ac0d3ae-063e-4789-93fe-3c73e93191b9"
    }
}
```

