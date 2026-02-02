**Example 1: 下线只读分析引擎**

下线只读分析引擎

Input: 

```
tccli cynosdb OfflineLibraDBInstance --cli-unfold-argument  \
    --ClusterId cynosdbmysql-bzxxrmtq \
    --InstanceIdList cynosdbmysql-libradb-ins-mhrc48ym
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

