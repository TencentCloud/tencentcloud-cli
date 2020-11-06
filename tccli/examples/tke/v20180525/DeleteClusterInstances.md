**Example 1: Deleting a Node in a Cluster**

Delete a node in a cluster

Input: 

```
tccli tke DeleteClusterInstances --cli-unfold-argument  \
    --ClusterId cls-xxxxxx \
    --InstanceIds ins-xxxxx \
    --InstanceDeleteMode terminate
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

