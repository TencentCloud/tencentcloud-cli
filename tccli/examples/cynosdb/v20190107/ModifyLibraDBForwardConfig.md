**Example 1: 修改分析实例转发配置**



Input: 

```
tccli cynosdb ModifyLibraDBForwardConfig --cli-unfold-argument  \
    --InstanceId libradb-ins-ex0klgmh \
    --ForwardMode AUTO \
    --ForwardList.0.InstanceId cynosdbmysql-ins-62lfwjfx \
    --ForwardList.0.Region ap-qingyuan
```

Output: 
```
{
    "Response": {
        "RequestId": "cbe293d6-fa37-46dc-a1f5-4781dd1af254"
    }
}
```

