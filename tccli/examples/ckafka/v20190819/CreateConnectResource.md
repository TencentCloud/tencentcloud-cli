**Example 1: 创建Datahub连接源(ES)**

创建Datahub连接源(ES)

Input: 

```
tccli ckafka CreateConnectResource --cli-unfold-argument  \
    --Description xxxx \
    --EsConnectParam.UserName elastic \
    --EsConnectParam.Resource es-xxx \
    --EsConnectParam.Password xxxx \
    --EsConnectParam.Port 9200 \
    --EsConnectParam.ServiceVip 10.0.0.1 \
    --EsConnectParam.UniqVpcId vpc-xxx \
    --EsConnectParam.SelfBuilt False \
    --ResourceName xxxx \
    --Type ES
```

Output: 
```
{
    "Response": {
        "Result": {
            "ResourceId": "resource-xx"
        },
        "RequestId": "xxxx"
    }
}
```

**Example 2: 创建Datahub连接源(DTS)**

创建Datahub连接源(DTS)

Input: 

```
tccli ckafka CreateConnectResource --cli-unfold-argument  \
    --Description xxxxx \
    --DtsConnectParam.UserName root \
    --DtsConnectParam.Resource dts-xxx \
    --DtsConnectParam.Topic topic \
    --DtsConnectParam.GroupId group \
    --DtsConnectParam.Password xxxx \
    --DtsConnectParam.Port 0 \
    --ResourceName xxxx \
    --Type DTS
```

Output: 
```
{
    "Response": {
        "Result": {
            "ResourceId": "resource-xx"
        },
        "RequestId": "xxxx"
    }
}
```

