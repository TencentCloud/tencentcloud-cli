**Example 1: 删除集群应用**

在应用市场中集群删除某个已安装应用

Input: 

```
tccli tke UninstallClusterRelease --cli-unfold-argument  \
    --Namespace lwj \
    --ClusterId cls-65r1c5nu \
    --Name app-05
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
            "Status": "pending-uninstall",
            "UpdatedTime": "2020-04-15T14:44:42Z"
        },
        "RequestId": "33483fde-efec-4d3c-8ff6-340d9dbc2d01"
    }
}
```

