**Example 1: 集群创建应用**

集群创建应用

Input: 

```
tccli tke CreateClusterRelease --cli-unfold-argument  \
    --ChartFrom tke \
    --Name app-05 \
    --ClusterId cls-65r1c5nu \
    --Namespace lwj \
    --Chart redis \
    --ChartVersion 10.5.3 \
    --ChartNamespace helm-public
```

Output: 
```
{
    "Response": {
        "Release": {
            "Condition": "",
            "CreatedTime": "2020-04-15T14:44:42Z",
            "ID": "0b49c73e-a2eb-41d7-8a9b-c0e61cf1aabb",
            "Name": "app-05",
            "Namespace": "lwj",
            "Status": "pending-install",
            "UpdatedTime": "2020-04-15T14:44:42Z"
        },
        "RequestId": "33483fde-efec-4d3c-8ff6-340d9dbc2d01"
    }
}
```

