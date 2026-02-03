**Example 1: 隔离只读分析引擎实例**

隔离只读分析引擎实例

Input: 

```
tccli cynosdb IsolateLibraDBInstance --cli-unfold-argument  \
    --InstanceIdList libradb-ins-mhrc48ym \
    --ClusterId cynosdbmysql-ins-bzkxxrmt
```

Output: 
```
{
    "Response": {
        "RequestId": "128046",
        "FlowId": 123,
        "DealNames": [
            "sads"
        ]
    }
}
```

