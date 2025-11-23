**Example 1: 添加端口服务资产**

添加端口数据

Input: 

```
tccli ctem CreatePort --cli-unfold-argument  \
    --CustomerId 100081 \
    --Port 3306 \
    --Asset db.test.com \
    --IsHighRisk True \
    --Ip 1.1.1.1 \
    --App mysql \
    --Service mysql
```

Output: 
```
{
    "Response": {
        "Id": 24838,
        "RequestId": "d4f06b4b-cc0c-431c-9314-75a0b6d4a760"
    }
}
```

