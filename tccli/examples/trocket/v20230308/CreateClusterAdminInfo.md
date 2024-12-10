**Example 1: 标准请求**

标准请求

Input: 

```
tccli trocket CreateClusterAdminInfo --cli-unfold-argument  \
    --ClusterId 1 \
    --ClusterStatus RUNNING \
    --ClusterVersion 1 \
    --Room 1 \
    --DeployEnv CLOUD \
    --Nameserver 1 \
    --AccessKey 1 \
    --SecretKey 1
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "bc959d81-16a1-449a-a89a-eb1a1b804260"
    }
}
```

