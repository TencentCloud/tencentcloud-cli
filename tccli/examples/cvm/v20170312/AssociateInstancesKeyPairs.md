**Example 1: Binding a CVM key pair**



Input: 

```
tccli cvm AssociateInstancesKeyPairs --cli-unfold-argument  \
    --InstanceIds ins-1e4r6y8i ins-3e56fg78\
    --KeyIds skey-4e5ty7i8
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

