**Example 1: 修改ip端口**



Input: 

```
tccli cynosdb ModifyVipVport --cli-unfold-argument  \
    --ClusterId cynosdbmysql-mwg7121e \
    --InstanceGrpId cynosdbmysql-grp-o48ssqs5 \
    --Vip 172.1.1.1
```

Output: 
```
{
    "Response": {
        "RequestId": "a5706353-296a-4992-ad07-ac4a48eeba43",
        "FlowId": 134983
    }
}
```

