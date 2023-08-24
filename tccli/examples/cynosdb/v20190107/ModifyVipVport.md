**Example 1: 修改ip端口**



Input: 

```
tccli cynosdb ModifyVipVport --cli-unfold-argument  \
    --ClusterId cynosdbmysql-asd \
    --InstanceGrpId cynosdbmysql-grp-qwe \
    --Vip xx.xx.xx.xx
```

Output: 
```
{
    "Response": {
        "RequestId": "128046",
        "FlowId": 123
    }
}
```

