**Example 1: 数据库示例**



Input: 

```
tccli apm DescribeTopologyNew --cli-unfold-argument  \
    --EndTime 1650683106 \
    --InstanceId apm-6xYKFXYxo \
    --DownLevel 1 \
    --UpLevel 1 \
    --ServiceName mock_project_db \
    --StartTime 1650610585 \
    --View db \
    --ServiceInstance apm-6xYKFXYxo
```

Output: 
```
{
    "Response": {
        "Edges": [
            {
                "Id": "tingyun-java-order-service_0",
                "Weight": 1,
                "Source": "tingyun-java-order-service",
                "Target": "0",
                "Duration": 4.76,
                "ErrRate": 0,
                "Qps": 13.27,
                "Type": "",
                "Color": "green",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "user-service_mock_project_db",
                "Weight": 1,
                "Source": "user-service",
                "Target": "mock_project_db",
                "Duration": 6.73,
                "ErrRate": 0,
                "Qps": 635.27,
                "Type": "",
                "Color": "green",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "tingyun-java-user-service_mock_project_db",
                "Weight": 1,
                "Source": "tingyun-java-user-service",
                "Target": "mock_project_db",
                "Duration": 5.3,
                "ErrRate": 0.819672131147541,
                "Qps": 32.53,
                "Type": "",
                "Color": "green",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "tingyun-java-stock-service_mock_project_db",
                "Weight": 1,
                "Source": "tingyun-java-stock-service",
                "Target": "mock_project_db",
                "Duration": 5.34,
                "ErrRate": 0.5376344086021506,
                "Qps": 37.2,
                "Type": "",
                "Color": "green",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "tingyun-java-order-service_mock_project_db",
                "Weight": 1,
                "Source": "tingyun-java-order-service",
                "Target": "mock_project_db",
                "Duration": 5.02,
                "ErrRate": 0.9852216748768473,
                "Qps": 13.53,
                "Type": "",
                "Color": "green",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "tingyun-java-market-service_mock_project_db",
                "Weight": 1,
                "Source": "tingyun-java-market-service",
                "Target": "mock_project_db",
                "Duration": 5.7,
                "ErrRate": 0.17152658662092624,
                "Qps": 38.87,
                "Type": "",
                "Color": "green",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "tingyun-java-delivery-service_mock_project_db",
                "Weight": 1,
                "Source": "tingyun-java-delivery-service",
                "Target": "mock_project_db",
                "Duration": 5.47,
                "ErrRate": 0,
                "Qps": 13.33,
                "Type": "",
                "Color": "green",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "stock-service_mock_project_db",
                "Weight": 1,
                "Source": "stock-service",
                "Target": "mock_project_db",
                "Duration": 8.57,
                "ErrRate": 0,
                "Qps": 966.53,
                "Type": "",
                "Color": "green",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "market-service_mock_project_db",
                "Weight": 1,
                "Source": "market-service",
                "Target": "mock_project_db",
                "Duration": 15.15,
                "ErrRate": 0,
                "Qps": 643.33,
                "Type": "",
                "Color": "green",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "java-order-service_mock_project_db",
                "Weight": 1,
                "Source": "java-order-service",
                "Target": "mock_project_db",
                "Duration": 1,
                "ErrRate": 0,
                "Qps": 0.07,
                "Type": "",
                "Color": "green",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "java-market-service_mock_project_db",
                "Weight": 1,
                "Source": "java-market-service",
                "Target": "mock_project_db",
                "Duration": 1,
                "ErrRate": 0,
                "Qps": 0.07,
                "Type": "",
                "Color": "green",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "java-delivery-service_mock_project_db",
                "Weight": 1,
                "Source": "java-delivery-service",
                "Target": "mock_project_db",
                "Duration": 1,
                "ErrRate": 0,
                "Qps": 0.07,
                "Type": "",
                "Color": "green",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "User_tingyun-java-stock-service",
                "Weight": 1,
                "Source": "User",
                "Target": "tingyun-java-stock-service",
                "Duration": 0,
                "ErrRate": 0,
                "Qps": 0,
                "Type": "virtual",
                "Color": "",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "User_stock-service",
                "Weight": 1,
                "Source": "User",
                "Target": "stock-service",
                "Duration": 0,
                "ErrRate": 0,
                "Qps": 0,
                "Type": "virtual",
                "Color": "",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "User_tingyun-java-delivery-service",
                "Weight": 1,
                "Source": "User",
                "Target": "tingyun-java-delivery-service",
                "Duration": 0,
                "ErrRate": 0,
                "Qps": 0,
                "Type": "virtual",
                "Color": "",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "User_tingyun-java-user-service",
                "Weight": 1,
                "Source": "User",
                "Target": "tingyun-java-user-service",
                "Duration": 0,
                "ErrRate": 0,
                "Qps": 0,
                "Type": "virtual",
                "Color": "",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "User_order-service",
                "Weight": 1,
                "Source": "User",
                "Target": "order-service",
                "Duration": 0,
                "ErrRate": 0,
                "Qps": 0,
                "Type": "virtual",
                "Color": "",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "User_user-service",
                "Weight": 1,
                "Source": "User",
                "Target": "user-service",
                "Duration": 0,
                "ErrRate": 0,
                "Qps": 0,
                "Type": "virtual",
                "Color": "",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "User_delivery-service",
                "Weight": 1,
                "Source": "User",
                "Target": "delivery-service",
                "Duration": 0,
                "ErrRate": 0,
                "Qps": 0,
                "Type": "virtual",
                "Color": "",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "User_market-service",
                "Weight": 1,
                "Source": "User",
                "Target": "market-service",
                "Duration": 0,
                "ErrRate": 0,
                "Qps": 0,
                "Type": "virtual",
                "Color": "",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "User_tingyun-java-order-service",
                "Weight": 1,
                "Source": "User",
                "Target": "tingyun-java-order-service",
                "Duration": 0,
                "ErrRate": 0,
                "Qps": 0,
                "Type": "virtual",
                "Color": "",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            },
            {
                "Id": "User_tingyun-java-market-service",
                "Weight": 1,
                "Source": "User",
                "Target": "tingyun-java-market-service",
                "Duration": 0,
                "ErrRate": 0,
                "Qps": 0,
                "Type": "virtual",
                "Color": "",
                "SqlRequestCount": 0,
                "SqlErrorRequestCount": 0
            }
        ],
        "Nodes": [
            {
                "Id": "0",
                "Weight": 1,
                "Name": "0",
                "Duration": 4.76,
                "ErrRate": 0,
                "Kind": "",
                "Qps": 13.27,
                "Type": "redis",
                "Size": "small",
                "Color": "green",
                "IsModule": true,
                "Position": {
                    "X": 0,
                    "Y": 0
                },
                "CanDrillDown": false,
                "Tags": null
            },
            {
                "Id": "tingyun-java-market-service",
                "Weight": 1,
                "Name": "tingyun-java-market-service",
                "Duration": 0,
                "ErrRate": 1.718213058419244,
                "Kind": "",
                "Qps": 38.8,
                "Type": "grpcserver",
                "Size": "small",
                "Color": "green",
                "IsModule": false,
                "Position": {
                    "X": 0,
                    "Y": 0
                },
                "CanDrillDown": false,
                "Tags": null
            },
            {
                "Id": "tingyun-java-user-service",
                "Weight": 1,
                "Name": "tingyun-java-user-service",
                "Duration": 0,
                "ErrRate": 2.479338842975207,
                "Kind": "",
                "Qps": 32.27,
                "Type": "grpcserver",
                "Size": "small",
                "Color": "green",
                "IsModule": false,
                "Position": {
                    "X": 0,
                    "Y": 0
                },
                "CanDrillDown": false,
                "Tags": null
            },
            {
                "Id": "java-order-service",
                "Weight": 1,
                "Name": "java-order-service",
                "Duration": 0,
                "ErrRate": 0,
                "Kind": "",
                "Qps": 0,
                "Type": "",
                "Size": "small",
                "Color": "green",
                "IsModule": false,
                "Position": {
                    "X": 0,
                    "Y": 0
                },
                "CanDrillDown": false,
                "Tags": null
            },
            {
                "Id": "order-service",
                "Weight": 1,
                "Name": "order-service",
                "Duration": 227.25,
                "ErrRate": 0,
                "Kind": "",
                "Qps": 318.53,
                "Type": "net/http",
                "Size": "small",
                "Color": "green",
                "IsModule": false,
                "Position": {
                    "X": 0,
                    "Y": 0
                },
                "CanDrillDown": false,
                "Tags": null
            },
            {
                "Id": "user-service",
                "Weight": 1,
                "Name": "user-service",
                "Duration": 10.81,
                "ErrRate": 0.07733408323959505,
                "Kind": "",
                "Qps": 948.27,
                "Type": "grpc",
                "Size": "middle",
                "Color": "green",
                "IsModule": false,
                "Position": {
                    "X": 0,
                    "Y": 0
                },
                "CanDrillDown": false,
                "Tags": null
            },
            {
                "Id": "java-delivery-service",
                "Weight": 1,
                "Name": "java-delivery-service",
                "Duration": 0,
                "ErrRate": 0,
                "Kind": "",
                "Qps": 0,
                "Type": "",
                "Size": "small",
                "Color": "green",
                "IsModule": false,
                "Position": {
                    "X": 0,
                    "Y": 0
                },
                "CanDrillDown": false,
                "Tags": null
            },
            {
                "Id": "mock_project_db",
                "Weight": 1,
                "Name": "mock_project_db",
                "Duration": 7.12,
                "ErrRate": 0.028001792114695338,
                "Kind": "",
                "Qps": 2380.8,
                "Type": "mysql",
                "Size": "bigLarge",
                "Color": "green",
                "IsModule": true,
                "Position": {
                    "X": 0,
                    "Y": 0
                },
                "CanDrillDown": false,
                "Tags": null
            },
            {
                "Id": "java-market-service",
                "Weight": 1,
                "Name": "java-market-service",
                "Duration": 0,
                "ErrRate": 0,
                "Kind": "",
                "Qps": 0,
                "Type": "",
                "Size": "small",
                "Color": "green",
                "IsModule": false,
                "Position": {
                    "X": 0,
                    "Y": 0
                },
                "CanDrillDown": false,
                "Tags": null
            },
            {
                "Id": "tingyun-java-stock-service",
                "Weight": 1,
                "Name": "tingyun-java-stock-service",
                "Duration": 0,
                "ErrRate": 3.763440860215054,
                "Kind": "",
                "Qps": 37.2,
                "Type": "grpcserver",
                "Size": "small",
                "Color": "green",
                "IsModule": false,
                "Position": {
                    "X": 0,
                    "Y": 0
                },
                "CanDrillDown": false,
                "Tags": null
            },
            {
                "Id": "delivery-service",
                "Weight": 1,
                "Name": "delivery-service",
                "Duration": 29.59,
                "ErrRate": 0,
                "Kind": "",
                "Qps": 319.27,
                "Type": "net/http",
                "Size": "small",
                "Color": "green",
                "IsModule": false,
                "Position": {
                    "X": 0,
                    "Y": 0
                },
                "CanDrillDown": false,
                "Tags": null
            },
            {
                "Id": "stock-service",
                "Weight": 1,
                "Name": "stock-service",
                "Duration": 33.19,
                "ErrRate": 0.2915249531477754,
                "Kind": "",
                "Qps": 960.47,
                "Type": "grpc",
                "Size": "middle",
                "Color": "green",
                "IsModule": false,
                "Position": {
                    "X": 0,
                    "Y": 0
                },
                "CanDrillDown": false,
                "Tags": null
            },
            {
                "Id": "tingyun-java-delivery-service",
                "Weight": 1,
                "Name": "tingyun-java-delivery-service",
                "Duration": 10.91,
                "ErrRate": 0,
                "Kind": "",
                "Qps": 13.33,
                "Type": "springcontroller",
                "Size": "small",
                "Color": "green",
                "IsModule": false,
                "Position": {
                    "X": 0,
                    "Y": 0
                },
                "CanDrillDown": false,
                "Tags": null
            },
            {
                "Id": "User",
                "Weight": 1,
                "Name": "User",
                "Duration": 0,
                "ErrRate": 0,
                "Kind": "",
                "Qps": 0,
                "Type": "virtual",
                "Size": "small",
                "Color": "darkGray",
                "IsModule": false,
                "Position": {
                    "X": 0,
                    "Y": 0
                },
                "CanDrillDown": false,
                "Tags": null
            },
            {
                "Id": "market-service",
                "Weight": 1,
                "Name": "market-service",
                "Duration": 17.46,
                "ErrRate": 1.5148371031334302,
                "Kind": "",
                "Qps": 321.27,
                "Type": "grpc",
                "Size": "small",
                "Color": "green",
                "IsModule": false,
                "Position": {
                    "X": 0,
                    "Y": 0
                },
                "CanDrillDown": false,
                "Tags": null
            },
            {
                "Id": "tingyun-java-order-service",
                "Weight": 1,
                "Name": "tingyun-java-order-service",
                "Duration": 80.74,
                "ErrRate": 23.88059701492537,
                "Kind": "",
                "Qps": 13.4,
                "Type": "springcontroller",
                "Size": "small",
                "Color": "red",
                "IsModule": false,
                "Position": {
                    "X": 0,
                    "Y": 0
                },
                "CanDrillDown": false,
                "Tags": null
            }
        ],
        "RequestId": "aad5307a-d2d7-4d55-a79b-d29938b13b51",
        "Selectors": null,
        "TopologyModifyFlag": 1
    }
}
```

