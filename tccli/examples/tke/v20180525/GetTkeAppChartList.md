**Example 1: 获取EKS支持的网络 AppChart列表**

获取EKS支持的网络 AppChart列表

Input: 

```
tccli tke GetTkeAppChartList --cli-unfold-argument  \
    --Kind network \
    --ClusterType eks
```

Output: 
```
{
    "Response": {
        "AppCharts": [
            {
                "Label": "{\"amd64\":\"true\",\"eks\":\"true\",\"kind\":\"network\",\"network\":\"true\",\"tke\":\"true\"}",
                "LatestVersion": "1.5.1",
                "Name": "ingressnginx"
            }
        ],
        "RequestId": "566fdd07-fa79-4dc1-8d22-78907dedd607"
    }
}
```

