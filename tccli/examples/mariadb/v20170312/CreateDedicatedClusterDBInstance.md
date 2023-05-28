**Example 1: 创建MariaDB独享集群实例**

创建MariaDB独享集群实例

Input: 

```
tccli mariadb CreateDedicatedClusterDBInstance --cli-unfold-argument  \
    --Zone ap-guangzhou-2 \
    --GoodsNum 1 \
    --Storage 10 \
    --Memory 2 \
    --ClusterId cage-shjr-2-10
```

Output: 
```
{
    "Response": {
        "RequestId": "14f6980a-7fe1-11ea-b896-525400542aa6",
        "InstanceIds": [
            "tdsql-xxxxxx"
        ],
        "FlowId": 1122
    }
}
```

