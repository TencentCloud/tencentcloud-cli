**Example 1: Acquiring the admin role of a cluster**

When a CAM admin sub-account is granted this action permission, it can acquire the cluster admin role through this API to access resources in the Kubernetes cluster.

Input: 

```
tccli tke AcquireClusterAdminRole --cli-unfold-argument  \
    --ClusterId cls-xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx"
    }
}
```

