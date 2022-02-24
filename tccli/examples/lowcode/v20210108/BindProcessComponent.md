**Example 1: 流程组件绑定**



Input: 

```
tccli lowcode BindProcessComponent --cli-unfold-argument  \
    --EnvId env-001 \
    --ProcessKeyList xx \
    --AppDeployLink https://app1xxxx.tcloudbaseapp.com//adminportal/#/app/appCode-001 \
    --AppCode appCode-001
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

