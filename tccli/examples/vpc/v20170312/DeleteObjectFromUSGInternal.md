**Example 1: 对象离开安全组**



Input: 

```
tccli vpc DeleteObjectFromUSGInternal --cli-unfold-argument  \
    --DelObjectsFromUSGRequest.0.UsgId sg-aosmqpxs \
    --DelObjectsFromUSGRequest.0.Vms 84f9a2ad-6659-4864-808c-bd17f3c2acea
```

Output: 
```
{
    "Response": {
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

