**Example 1: 创建Datahub连接源(ES)**

创建Datahub连接源(ES)

Input: 

```
tccli ckafka CreateConnectResource --cli-unfold-argument  \
    --Description your description \
    --EsConnectParam.UserName elastic \
    --EsConnectParam.Resource es-test \
    --EsConnectParam.Password yourpassword \
    --EsConnectParam.Port 9200 \
    --EsConnectParam.ServiceVip 10.0.0.1 \
    --EsConnectParam.UniqVpcId vpc-test \
    --EsConnectParam.SelfBuilt False \
    --ResourceName yourresourcename \
    --Type ES
```

Output: 
```
{
    "Response": {
        "Result": {
            "ResourceId": "resource-test"
        },
        "RequestId": "9e6d209b-69fd-4a00-b064-75131aa0a0f8"
    }
}
```

**Example 2: 创建Datahub连接源(DTS)**

创建Datahub连接源(DTS)

Input: 

```
tccli ckafka CreateConnectResource --cli-unfold-argument  \
    --Description your description \
    --DtsConnectParam.UserName root \
    --DtsConnectParam.Resource dts-test \
    --DtsConnectParam.Topic topic \
    --DtsConnectParam.GroupId group \
    --DtsConnectParam.Password yourpassword \
    --DtsConnectParam.Port 0 \
    --ResourceName resourcename \
    --Type DTS
```

Output: 
```
{
    "Response": {
        "Result": {
            "ResourceId": "resource-test"
        },
        "RequestId": "9e6d209b-69fd-4a00-b064-75131aa0a0f8"
    }
}
```

