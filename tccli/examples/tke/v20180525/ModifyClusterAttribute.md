**Example 1: Modifying cluster attributes**



Input: 

```
tccli tke ModifyClusterAttribute --cli-unfold-argument  \
    --ClusterId cls-xxxxxxx \
    --ClusterName aaa
```

Output: 
```
{
    "Response": {
        "ClusterName": "xxxxx",
        "ClusterDesc": "xxxxx",
        "ProjectId": 0,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459398"
    }
}
```

