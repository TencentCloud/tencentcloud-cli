**Example 1: 创建Datahub连接源(DTS)**



Input: 

```
tccli ckafka CreateConnectResource --cli-unfold-argument  \
    --Description xx \
    --DtsConnectParam.UserName root \
    --DtsConnectParam.Resource dts-xxx \
    --DtsConnectParam.Topic topic \
    --DtsConnectParam.GroupId group \
    --DtsConnectParam.Password xx \
    --DtsConnectParam.Port 0 \
    --ResourceName xx \
    --Type DTS
```

Output: 
```
{
    "Response": {
        "Result": {
            "ResourceId": "resource-xx"
        },
        "RequestId": "xx"
    }
}
```

**Example 2: 创建Datahub连接源(ES)**



Input: 

```
tccli ckafka CreateConnectResource --cli-unfold-argument  \
    --Description xx \
    --EsConnectParam.UserName elastic \
    --EsConnectParam.Resource es-xxx \
    --EsConnectParam.Password xx \
    --EsConnectParam.Port 9200 \
    --EsConnectParam.ServiceVip 10.0.0.1 \
    --EsConnectParam.UniqVpcId vpc-xxx \
    --EsConnectParam.SelfBuilt False \
    --ResourceName xx \
    --Type ES
```

Output: 
```
{
    "Response": {
        "Result": {
            "ResourceId": "resource-xx"
        },
        "RequestId": "xx"
    }
}
```

